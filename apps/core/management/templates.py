from functools import cached_property
from django.conf import settings
import os


class BaseTemplate:
    FILES = []
    ROOT = ""

    def __init__(self, parent_dir="", root="", ignore_parent=False):
        self.ignore_parent = ignore_parent
        self.parent_dir = parent_dir
        if root:
            self.ROOT = root

    @cached_property
    def dirs(self):
        if not self.parent_dir and self.ignore_parent == False:
            raise TypeError(
                "You must either provide a parent dir or set ignore_parent to True"
            )

        return [
            (
                self.parent_dir / self.ROOT / "/".join(x.split("/")[:-1]),
                x.split("/")[-1],
            )
            for x in self.FILES
        ]

    @cached_property
    def write_only_dirs(self):
        if not self.parent_dir and self.ignore_parent == False:
            raise TypeError(
                "You must either provide a parent dir or set ignore_parent to True"
            )

        return [
            (
                self.BASE_DIR / "/".join(x.split("/")[:-1]),
                x.split("/")[-1],
            )
            for x in self.FILES
        ]

    def make_template(self):
        try:
            os.mkdir(self.parent_dir / self.ROOT)
        except FileNotFoundError:
            raise FileNotFoundError(f"No such app in directory '{self.parent_dir}'")
        except FileExistsError:
            raise FileExistsError(
                f"The api in already setup in directory: '{self.parent_dir}'"
            )

        for dir in self.dirs:
            dir = tuple(map(lambda x: str(x), dir))
            print(dir)
            self.make_parent_dirs(dir[0])
            try:
                print("/".join(dir))
                os.mknod("/".join(dir))
            except FileExistsError:
                pass
        self.write_data()
        self.extra_write()

    def extra_write(self):
        ...

    def make_parent_dirs(self, dir: str):
        dir = dir.split("/")
        for i, j in enumerate(dir):
            try:
                os.mkdir("/".join(dir[: i + 1]) + "/")
            except FileExistsError:
                continue

    def write_data(self):
        for i in self.dirs:
            attr_name = f"{i[1].replace('/', '_').replace('.py', '')}_write"
            if hasattr(self, attr_name):
                attr = getattr(self, attr_name)
                self.perform_write(attr, i[0] / i[1])

    def perform_write(self, func, dir):
        func(dir)

    def append_file(self, file: str, data: str, overwrite=False):
        with open(f"{file}", "r+") as f:
            if overwrite:
                file_data = f.read()
                if not data in file_data:
                    f.write(f"\n{data}")
            else:
                f.write(data)

    def write_file(self, file: str, data: str):
        with open(f"{file}", "w") as f:
            f.write(data)

    def replace_file(self, file: str, data: list):
        with open(f"{file}", "r+") as f:
            file_data = f.read()
            replace_data = data

            if not isinstance(data, list):
                raise TypeError(
                    "data must be instance of list containing tuples which represent new and old values"
                )

            for i in replace_data:
                file_data = file_data.replace(*i)

            f.truncate()
            f.seek(0)
            f.write(file_data)


class ApiTemplate(BaseTemplate):
    FILES = ["views.py", "serializers.py", "urls.py"]
    ROOT = "api"

    def views_write(self, file):
        self.write_file(file, "from rest_framework.viewsets import ModelViewSet")

    def extra_write(self):
        self.append_file(
            os.path.join(settings.BASE_DIR, "requirements/base.txt"),
            "djangorestframework==3.13.1",
            True,
        )
