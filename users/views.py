""" Users views. """
# Django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Models
from django.contrib.auth.models import User
from users.models import Profile

# Forms
from users.forms import ProfileForm

# Exception
from django.db.utils import IntegrityError


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

@login_required
def logout_view(request):
    """ Logout a user. """
    logout(request)
    return redirect('login')

def signup_view(request):
    """ Sign up view. """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirmation = request.POST.get('password_confirmation')

        if password != password_confirmation:
            return render(request, 'users/signup.html', {
                'error': 'Password confirmation does not match.',
            })
        try:
            user = User.objects.create_user(username=username, password=password)
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            user.email = request.POST.get('email')
            user.save()
        except IntegrityError:
            return render(request, 'users/signup.html', {
                'error': 'Username is already in user.',
            })
        
        profile = Profile(user=user)
        profile.save()

        return redirect('login')

    return render(request, 'users/signup.html')

@login_required
def update_profile(request):
    """ Update a user's profile view. """
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        # Verificamos que los datos ingresados
        # por el usuario sean correctos
        if form.is_valid():
            data = form.cleaned_data
            profile.website = data['website']
            profile.phone_number = data['phone_number']
            profile.biography = data['biography']
            profile.picture = data['picture']
            profile.save()
            
            return redirect('update_profile')
    else:
        form = ProfileForm()

    return render(request, 'users/update_profile.html', {
        'profile': profile,
        'user': request.user,
        'form': form
    })
