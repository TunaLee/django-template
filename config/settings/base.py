"""
Base settings to build other settings files upon.
"""
# Python
import environ

# Django
from django.utils.translation import ugettext_lazy as _

# Third Party
from pathlib import Path
from typing import List
from corsheaders.defaults import default_methods

ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent.parent
# django_template/
APPS_DIR = ROOT_DIR / "django_template"
env = environ.Env()

# ENVIRONMENT
# ---------------------------------------------------------------------------------
DJANGO_SETTINGS_MODULE = env("DJANGO_SETTINGS_MODULE")
print('DJANGO_SETTINGS_MODULE : ', DJANGO_SETTINGS_MODULE)

DJANGO_ENV = DJANGO_SETTINGS_MODULE.split(".")[-1]  # config.settings.(.+)
print(f"Running server using {DJANGO_ENV} settings")

# If current environment is local, read all files in .envs/.local to make it handy
# of using other environment variables. Also, read .env file by default too.
#
# Note: OS environment variables take precedence over variables from .env
env_files_to_read: List[Path] = []
if DJANGO_ENV == "local":
    local_env_dir = ROOT_DIR / ".envs" / ".local"
    if local_env_dir.exists():
        env_files_to_read.extend(local_env_dir.iterdir())

    READ_DOT_ENV_FILE = env.bool("DJANGO_READ_DOT_ENV_FILE", default=True)
    if READ_DOT_ENV_FILE:
        dot_env_file = ROOT_DIR / ".env"
        env_files_to_read.append(dot_env_file)
else:
    # Read only necessary file for non-local environment.
    django_env_file = ROOT_DIR / ".envs" / f".{DJANGO_ENV}" / ".django"
    env_files_to_read.append(django_env_file)

files_not_exist = []
for f in env_files_to_read:
    if f.exists():
        print(f"Reading environments from {f!s}")
        env.read_env(str(f))
    else:
        files_not_exist.append(f)

if files_not_exist:
    print("{} file(s) does not exists: {}".format(len(files_not_exist), ", ".join(map(str, files_not_exist))))

print("")

# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool("DJANGO_DEBUG", False)
# Local time zone. Choices are
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# though not all of them may be available with every OS.
# In Windows, this must be set to your system time zone.
TIME_ZONE = "Asia/Seoul"
# https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = "en-us"
# https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1
# https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True
# https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True
# https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = False
# https://docs.djangoproject.com/en/dev/ref/settings/#locale-paths
LOCALE_PATHS = [str(ROOT_DIR / "locale")]

# DATABASES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    "default": env.db(
        "DATABASE_URL",
        default="",
    ),
}
DATABASES["default"]["ATOMIC_REQUESTS"] = True
# https://docs.djangoproject.com/en/stable/ref/settings/#std:setting-DEFAULT_AUTO_FIELD
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

print('DATABASES : ', DATABASES)

# URLS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = "config.urls"
# https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = "config.wsgi.application"

# APPS
# ------------------------------------------------------------------------------
DJANGO_APPS = [
    'jet',
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.admin",
    "django.forms",
]

THIRD_PARTY_APPS = [
    # Django Model
    "phonenumber_field",
    "django_redis",

    # Django Form
    "crispy_forms",

    # Django Admin
    "admin_reorder",
    "django_admin_relation_links",
    "nested_admin",
    "import_export",
    "inline_actions",
    "rangefilter",
    'nested_inline',
    "admin_numeric_filter",

    # django-allauth
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.kakao",
    "allauth.socialaccount.providers.apple",

    # django-rest-framework
    "rest_framework",
    "rest_framework.authtoken",
    "corsheaders",
    "django_filters",
    "drf_extra_fields",
    "drf_yasg",
    "url_filter",

    # django-health-check
    "health_check",
    "health_check.db",
    "health_check.storage",
    "health_check.contrib.migrations",
    "health_check.contrib.psutil",
]

LOCAL_APPS = [
    "django_template.apps.app_templates.apps.ViewsConfig",
    "django_template.apps.users.apps.UsersConfig",
]
# https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# MIGRATIONS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#migration-modules
MIGRATION_MODULES = {"sites": "django_template.contrib.sites.migrations"}

# AUTHENTICATION
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#authentication-backends
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-user-model
AUTH_USER_MODEL = "users.User"
# https://docs.djangoproject.com/en/dev/ref/settings/#login-redirect-url
LOGIN_REDIRECT_URL = "users:redirect"
# https://docs.djangoproject.com/en/dev/ref/settings/#login-url
LOGIN_URL = "account_login"

# PASSWORDS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#password-hashers
PASSWORD_HASHERS = [
    # https://docs.djangoproject.com/en/dev/topics/auth/passwords/#using-argon2-with-django
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
    # {'NAME': 'django_template.utils.validators.CustomPasswordValidator'},
]

# MIDDLEWARE
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    # "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.common.BrokenLinkEmailsMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'admin_reorder.middleware.ModelAdminReorder',
]

# # STATIC
# # ------------------------------------------------------------------------------
# # https://docs.djangoproject.com/en/dev/ref/settings/#static-root
# STATIC_ROOT = str(ROOT_DIR / "staticfiles")
# # https://docs.djangoproject.com/en/dev/ref/settings/#static-url
# STATIC_URL = "/static/"
# # https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
# STATICFILES_DIRS = [str(APPS_DIR / "static")]
# # https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
# STATICFILES_FINDERS = [
#     "django.contrib.staticfiles.finders.FileSystemFinder",
#     "django.contrib.staticfiles.finders.AppDirectoriesFinder",
# ]

# MEDIA
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = str(APPS_DIR / "media")
# https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = "/media/"

# TEMPLATES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        # https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES-BACKEND
        "BACKEND": "django.django_template.backends.django.DjangoTemplates",
        # https://docs.djangoproject.com/en/dev/ref/settings/#dirs
        "DIRS": [str(APPS_DIR / "templates")],
        # https://docs.djangoproject.com/en/dev/ref/settings/#app-dirs
        "APP_DIRS": True,
        "OPTIONS": {
            # https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
            "context_processors": [
                "django.django_template.context_processors.debug",
                "django.django_template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.django_template.context_processors.i18n",
                "django.django_template.context_processors.media",
                "django.django_template.context_processors.static",
                "django.django_template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                "han-duck.utils.context_processors.settings_context",
            ],
        },
    }
]

# https://docs.djangoproject.com/en/dev/ref/settings/#form-renderer
FORM_RENDERER = "django.forms.renderers.TemplatesSetting"

# http://django-crispy-forms.readthedocs.io/en/latest/install.html#template-packs
CRISPY_TEMPLATE_PACK = "bootstrap5"
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

# FIXTURES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#fixture-dirs
FIXTURE_DIRS = (str(APPS_DIR / "fixtures"),)

# SECURITY
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-httponly
SESSION_COOKIE_HTTPONLY = True
# https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-httponly
CSRF_COOKIE_HTTPONLY = True
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-browser-xss-filter
SECURE_BROWSER_XSS_FILTER = True
# https://docs.djangoproject.com/en/dev/ref/settings/#x-frame-options
X_FRAME_OPTIONS = "DENY"

# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND",
    default="django.core.mail.backends.smtp.EmailBackend",
)
# https://docs.djangoproject.com/en/dev/ref/settings/#email-timeout
EMAIL_TIMEOUT = 5

# ADMIN
# ------------------------------------------------------------------------------
# Django Admin URL.
ADMIN_URL = "admin/"
# https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = [("""Tuna Lee""", "dongwon1103@gmail.com")]
# https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS

ADMIN_REORDER = (
    # Keep original label and models
    'users', 'app_templates'
    # # Rename app
    # {'app': 'auth', 'label': 'Authorisation'},
    # # Reorder app models
    # {'app': 'auth', 'models': ('auth.User', 'auth.Group')},
    # # Exclude models
    # {'app': 'auth', 'models': ('auth.User', )},
    # # Cross-linked models
    # {'app': 'auth', 'models': ('auth.User', 'sites.Site')},
    # # models with custom name
    # {'app': 'auth', 'models': (
    #     'auth.Group',
    #     {'model': 'auth.User', 'label': 'Staff'},
    # )},
)

# LOGGING
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#logging
# See https://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s "
            "%(process)d %(thread)d %(message)s"
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    "root": {"level": "INFO", "handlers": ["console"]},
}


# django-allauth
# ------------------------------------------------------------------------------
ACCOUNT_ALLOW_REGISTRATION = env.bool("DJANGO_ACCOUNT_ALLOW_REGISTRATION", True)
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_AUTHENTICATION_METHOD = "email"
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_EMAIL_REQUIRED = True
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_ADAPTER = "django_template.apps.users.adapters.AccountAdapter"
# https://django-allauth.readthedocs.io/en/latest/forms.html
ACCOUNT_FORMS = {"signup": "django_template.apps.users.forms.UserSignupForm"}
# https://django-allauth.readthedocs.io/en/latest/configuration.html
SOCIALACCOUNT_ADAPTER = "django_template.apps.users.adapters.SocialAccountAdapter"
# https://django-allauth.readthedocs.io/en/latest/forms.html
SOCIALACCOUNT_FORMS = {"signup": "django_template.apps.users.forms.UserSocialSignupForm"}

# django-rest-framework
# -------------------------------------------------------------------------------
# django-rest-framework - https://www.django-rest-framework.org/api-guide/settings/
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.AllowAny",),
    "EXCEPTION_HANDLER": "django_template.utils.exception_handlers.custom_exception_handler",
    "NON_FIELD_ERRORS_KEY": "non_field_errors",
}

# django-cors-headers - https://github.com/adamchainz/django-cors-headers#setup
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_METHODS = default_methods

# Your stuff...
# ------------------------------------------------------------------------------

# django-health-check
# ------------------------------------------------------------------------------------
# https://pypi.org/project/django-health-check/
HEALTH_CHECK = {
    "DISK_USAGE_MAX": 90,  # percent
    "MEMORY_MIN": 100,  # in MB
}

# django-phonenumber-field
# --------------------------------------------------------------------------------
# https://github.com/stefanfoulis/django-phonenumber-field
PHONENUMBER_DEFAULT_REGION = "KR"
PHONENUMBER_DEFAULT_FORMAT = "NATIONAL"

# django-admin-charts
# ------------------------------------------------------------------------------
ADMIN_CHARTS_NVD3_JS_PATH = "bow/nvd3/build/nv.d3.js"
ADMIN_CHARTS_NVD3_CSS_PATH = "bow/nvd3/build/nv.d3.css"
ADMIN_CHARTS_D3_JS_PATH = "bow/d3/d3.js"

# drf-yasg
# ------------------------------------------------------------------------------------
# https://drf-yasg.readthedocs.io/en/stable/settings.html
SWAGGER_SETTINGS = {
    "DEFAULT_AUTO_SCHEMA_CLASS": "django_template.utils.api.schema.CustomAutoSchema",
    "SECURITY_DEFINITIONS": {
        "Token": {
            "type": "apiKey",
            "description": _(
                """서버에서 발급한 토큰을 기반으로 한 인증 방식입니다. 'Token NTY3ODkwIiwibmFtZSI6I...'와 같이 입력해주세요.<br/>
                   토큰이 세션보다 우선적으로 사용됩니다.<br/>"""
            ),
            "name": "Authorization",
            "in": "header",
        },
    },
    'OPERATIONS_SORTER': 'method',
    'TAGS_SORTER': 'alpha',
}
