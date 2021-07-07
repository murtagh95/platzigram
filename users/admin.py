""" Users admin classes. """
# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Models
from django.contrib.auth.models import User
from users.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """ Profile admin. """
    # Campos visibles en la vista Lista
    list_display = ('pk', 'user', 'phone_number', 'website', 'picture')
    # Campos que llevan a la vista Formulario
    list_display_links = ('pk', 'user')
    # Campos que se pueden editar en la vista Lista
    list_editable = ('phone_number', 'website', 'picture')
    # Campos por los cuales se puede buscar
    search_fields = (
        'user__email',
        'user__username',
        'user__first_name',
        'user__last_name',
        'phone_number'
    )
    # Campos que se pueden filtrar
    list_filter = (
        'user__is_active',
        'user__is_staff',
        'created',
        'modified',
    )

    # Configuro la vista Formulario
    fieldsets = (
        ('Profile', {  # Primer argumento el título
            'fields': (('user', 'picture'),)  # Campos que se mostraran
        }),
        ('Extrainfo', {
            'fields': (
                ('website', 'phone_number'),
                ('biography')
            )
        }),
        ('Metadata', {
            'fields': (('created', 'modified'))
        })
    )
    # Campos de solo lectura
    readonly_fields = ('created', 'modified', 'user')


class ProfileInLine(admin.StackedInline):
    """ Profile in-line admin for users. """
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'


class UserAdmin(BaseUserAdmin):
    """ Add profile admin to vase user admin. """
    inlines = (ProfileInLine,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff',
    )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
