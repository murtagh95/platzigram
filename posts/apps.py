from django.apps import AppConfig


class PostsConfig(AppConfig):
    """ Configuración de la aplicación Posts """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'posts'
    verbose_name= 'Posts'
