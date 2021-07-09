""" Users views. """
# Django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_view(request):
    """ Login view. """
    # import pdb; pdb.set_trace()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Verifico las credenciales de acceso ingresadas
        # Si son correctas me devuelve el usuario
        user = authenticate(
            request,
            username=username,
            password=password
        )
        if user:
            login(request, user)
            # Lo rederijimos a posts
            return redirect('feed')
        else:
            return render(request, "users/login.html", {
                'error': 'Invalid username and password'
            })


    return render(request, "users/login.html")
