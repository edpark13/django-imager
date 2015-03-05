from django.apps import AppConfig


class MyAppConfig(AppConfig):

    name = 'profiles'

    def ready(self):
        """Perform configuration that must happen at startup time."""
        import signals
