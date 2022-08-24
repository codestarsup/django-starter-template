from functools import cached_property
import os


class BaseTemplate:
    FILES = []
    ROOT = ""

    class WriteMode:
        APPEND = "a"
        REWRITE = "w"
        REPLACE = "r"

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

        return [(self.parent_dir / self.ROOT, x) for x in self.FILES]

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
            dir = tuple(map(lambda x: str(x), dir))
            self.make_parent_dirs(dir[0])
            os.mknod(dir[1])
            self.write_data()

    def write_data(self):
        for i in self.FILES:
            attr_name = f"{i.replace('/', '_').replace('.py', '')}_write"
            if hasattr(self, attr_name):
                attr = getattr(self, attr_name)
                write_data = attr()
                try:
                    write_mode = write_data["mode"]
                    data = write_data["data"]
                except KeyError:
                    raise Exception(
                        f'Write function must return a dictionary containing "data" and "mode" keys.'
                    )

                # VALIDATE IF FUNCTION IS RETURNING WHAT WE NEED
                self.validate_write(write_data)

                if write_mode == BaseTemplate.WriteMode.APPEND:
                    with open(f"{i}", "a") as f:
                        f.write(data)

                elif write_mode == BaseTemplate.WriteMode.REWRITE:
                    with open(f"{i}", "w") as f:
                        f.write(data)

                elif write_mode == BaseTemplate.WriteMode.REPLACE:
                    with open(f"{i}", "r+") as f:
                        file_data = f.read()
                        try:
                            replace_data = write_data["replace"]
                        except:
                            raise Exception(
                                "In replace mode write function returning dictionary"
                                "must contain a key named 'replace' which is a tuple (old, new)"
                            )

                        for i in replace_data:
                            file_data = file_data.replace(*i)

                        f.truncate()
                        f.seek(0)
                        f.write(file_data)


class ApiFilesTemplate(BaseTemplate):
    FILES = ["views.py", "serializers.py", "urls.py"]
    ROOT = "api"

    def views_write(self):
        context = {"mode": self.WriteMode.REWRITE, "s": ""}
