from django.apps import AppConfig


class AnnouncementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.announcement'
    verbose_name = 'Объявление'

    def ready(self):
        import apps.announcement.signals
