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

    def make_template(self):
        os.mkdir(self.parent_dir / self.ROOT)

        for dir in self.dirs:
            os.mknod(dir)


class ApiTemplate(BaseTemplate):
    FILES = [
        "views.py",
        "serializers.py",
        "urls.py",
    ]
    ROOT = "api"
