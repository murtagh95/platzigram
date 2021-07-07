""" Posts models. """

# Django
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """ Post model. """
    
    title = models.CharField(max_length=255)

    photo =  models.ImageField(
        upload_to='posts/photos',
        blank=True,
        null=True
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)

    # Cuando se crea el registro le asigna el valor de manera auto
    created = models.DateTimeField(auto_now_add=True)  
    #  Cuando se modifique un campo del registro se guardara la fecha auto
    modified = models.DateTimeField(auto_now=True)

    def __str__(slef):
        """ Return title and username. """
        return f"{self.title} by @{self.user.username}"
