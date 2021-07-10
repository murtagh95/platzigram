""" Platzigram middleware catalog. """ 

# Django
from django.shortcuts import redirect
from django.urls import reverse

class ProfileCompletionMiddleware:
    """ Profile completion middleware. 
    Ensure every user that is interacting with the platform
    have their profile picture and biography.
    """
    def __init__(self, get_response):
        """ Middleware initialization.  """
        self.get_response = get_response
    

    def __call__(self, request):
        """ Code to be execute for each request before the
        view is called. """
        # Verifico que este logeado el usuario
        if not request.user.is_anonymous:
            if not request.user.is_staff:
                profile = request.user.profile
                if not profile.picture or not profile.biography:
                    # Verifico que no se encuentre en la vista para
                    # actualizar el perfil sino se queda en un bucle infi
                    if request.path not in [
                        reverse('update_profile'),
                        reverse('logout')
                    ] :
                        return redirect("update_profile")
        
        response = self.get_response(request)
        return response 
