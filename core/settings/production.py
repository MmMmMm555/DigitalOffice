# import sentry_sdk
# from sentry_sdk.integrations.django import DjangoIntegration
# from sentry_sdk.integrations.celery import CeleryIntegration

from .base import *  # noqa

###################################################################
# General
###################################################################

DEBUG = True

###################################################################
# Django security
###################################################################

"""
IF YOU WANT SET CSRF_TRUSTED_ORIGINS = ["*"] THEN YOU SHOULD SET:
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
"""


# CSRF_TRUSTED_ORIGINS = [
#     "http://localhost:5173",
# ]

###################################################################
# CORS

# CORS_ALLOWED_ORIGINS = ['http://localhost:5173', ]

###################################################################

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]
CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_SECURE_ALL = True
CORS_ALLOW_ALL_ORIGINS = True
# init sentry
# sentry_sdk.init(
#     dsn=env.str("SENTRY_DSN", default=""),  # noqa
#     integrations=[DjangoIntegration(), CeleryIntegration()],
#     # Set traces_sample_rate to 1.0 to capture 100%
#     # of transactions for performance monitoring.
#     # We recommend adjusting this value in production.
#     traces_sample_rate=1.0,
#     # If you wish to associate users to errors (assuming you are using
#     # django.contrib.auth) you may enable sending PII data.
#     send_default_pii=True,
# )
# end init sentry
