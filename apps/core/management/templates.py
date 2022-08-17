from functools import cached_property
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

        return [self.parent_dir / self.ROOT / x for x in self.FILES]

    def validate(self, dirs: list):
        ...

    def make_parent_dirs(self, dir: str):
        dir = dir.split("/")
        for i, j in enumerate(dir):
            try:
                os.mkdir("/".join(dir[: i + 1]) + "/")
            except FileExistsError:
                continue

    def make_template(self):

        self.validate(self.dirs)

        try:
            os.mkdir(self.parent_dir / self.ROOT)
        except FileNotFoundError:
            raise FileNotFoundError(f"No such app in directory '{self.parent_dir}'")
        except FileExistsError:
            raise FileExistsError(
                f"The api in already setup in directory: '{self.parent_dir}'"
            )
        except Exception as e:
            raise e

        for dir in self.dirs:
            dir = str(dir)
            if "/" in dir:
                last_slash = dir.rfind("/")
                self.make_parent_dirs(dir[:last_slash])
            os.mknod(dir)


class ApiTemplate(BaseTemplate):
    FILES = ["views.py", "serializers.py", "urls.py"]
    ROOT = "api"
