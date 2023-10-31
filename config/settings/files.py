from .handler import BASE_DIR

# Static files (CSS, JavaScript, Images)
STATIC_URL = "static/"

STATIC_ROOT = BASE_DIR / "staticfiles"
STATIC_ROOT = env.str("PUBLIC_STATIC_ROOT", STATIC_ROOT) # This ENV variable will be used in the CI/CD

STATICFILES_DIRS = [BASE_DIR / "static"]
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# MEDIA
MEDIA_ROOT = BASE_DIR / "media"
MEDIA_ROOT = env.str("PUBLIC_MEDIA_ROOT", MEDIA_ROOT) # This ENV variable will be used in the CI/CD
MEDIA_URL = "/media/"
