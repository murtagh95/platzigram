""" Posts URLs. """

# Django
from django.urls import path
from django.views.generic import TemplateView

# Views
from users import views


urlpatterns = [
    # Management
    path(route='me/profile/',
         view=views.update_profile,
         name='update_profile'),
    path(route='login',
         view=views.login_view,
         name='login'),
    path(route='logout',
         view=views.logout_view,
         name='logout'),
    path(route='signup',
         view=views.signup_view,
         name='signup'),
    # Posts
    path(route='<str:username>',
         view=TemplateView.as_view(template_name='users/detail.html'),
         name='datail'),
]

