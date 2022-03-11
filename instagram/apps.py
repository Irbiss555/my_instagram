from django.apps import AppConfig


class InstagramConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'instagram'

    def ready(self):
        print("at ready")
        import instagram.signals
