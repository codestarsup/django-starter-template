import shutil

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings


class Command(BaseCommand):
    help = (
        "Remove app by giving app name or giving app directory-"
        "if is not in APPS_DIR directory."
    )

    def add_arguments(self, parser):
        parser.add_argument(
            "appname",
            type=str,
            help="Name of the application to be deleted",
        )
        parser.add_argument(
            "--appdir", type=str, help="Directory that application lives in"
        )

    def handle(self, *args, **kwargs):
        app_name = kwargs.get("appname")
        app_dir = kwargs.get("appdir")
        is_default = True if (app_name and not app_dir) else False

        if not app_name:
            raise CommandError(
                "You must either define appname or both appname and appdir"
            )

        if is_default:
            parent_dir = settings.BASE_DIR / settings.APPS_DIR
        else:
            parent_dir = app_dir

        dir = parent_dir / app_name

        try:
            shutil.rmtree(dir)
        except FileNotFoundError:
            raise CommandError(
                "No application named {appname} in the '{parent_dir}' directory exists!"
            )
