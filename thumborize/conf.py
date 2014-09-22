from django.conf import settings

THUMBOR_SERVER = getattr(settings, "THUMBOR_SERVER",
                         "http://localhost:8888/").rstrip("/")

THUMBOR_SECURITY_KEY = getattr(settings, "THUMBOR_SECURITY_KEY", "MY_SECURE_KEY")

THUMBOR_DEFAULT_FILTERS = getattr(settings, "THUMBOR_DEFAULT_FILTERS", {})
