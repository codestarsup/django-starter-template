from django.core.management.base import CommandError, BaseCommand
from config.settings.apps import LOCAL_APPS
from django.apps import apps


class Command(BaseCommand):
    help = "A command to setup api for an application in APPS_DIR or given directory"

    def add_arguments(self, parser):
        parser.add_argument(
            "appname",
            type=str,
            help="The current Django project folder name",
            default=None,
        )

    def format_warning(self, msg: str, type: str = None):
        if type == "str":
            return self.style.WARNING(f"Warning: Model {msg} has not __str__ method.")

    def handle(self, *args, **options):
        app_name = options.get("appname")

        if app_name:
            try:
                app = apps.get_app_config(app_name)
            except LookupError:
                raise CommandError(
                    f"LookupError: No installed app with label '{app_name}'"
                )
            models = app.get_models()
            warnings = [
                self.format_warning(model, type="str")
                for model in models
                if not "__str__" in model.__dict__
            ]

            if warnings:
                self.stdout.write("\n".join(warnings))

        else:
            for app in LOCAL_APPS:
                try:
                    app = apps.get_app_config(app_name)
                except LookupError:
                    raise CommandError(
                        f"LookupError: No installed app with label '{app_name}'"
                    )
