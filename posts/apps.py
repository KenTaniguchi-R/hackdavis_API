from django.apps import AppConfig
from django.db.models.signals import post_migrate


class PostsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'posts'


    def ready(self):
        from .management import save_default
        post_migrate.connect(save_default, sender=self)
