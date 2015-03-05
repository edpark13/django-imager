from django.apps import AppConfig


class MyAppConfig(AppConfig):

    name = 'profiles'

    def ready(self):
        import signals
