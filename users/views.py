""" Users views. """
# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.urls import reverse

# Models
from django.contrib.auth.models import User

# Forms
from posts.models import Post
from users.forms import ProfileForm, SignupForm


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
            return redirect('posts:feed')
        else:
            return render(request, "users/login.html", {
                'error': 'Invalid username and password'
            })


    return render(request, "users/login.html")

@login_required
def logout_view(request):
    """ Logout a user. """
    logout(request)
    return redirect('users:login')

def signup_view(request):
    """ Sign up view. """
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('users:login')
        
    else:
        form = SignupForm()

    return render(request, 'users/signup.html', {
            'form': form
    })

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

            # Creamos la url que se puede rederijir
            url = reverse('users:datail', kwargs={
                'username': request.user.username
            })
            return redirect(url)
    else:
        form = ProfileForm()

    return render(request, 'users/update_profile.html', {
        'profile': profile,
        'user': request.user,
        'form': form
    })

class UserDetailView(LoginRequiredMixin, DetailView):
    """ User detail view. """

    template_name = 'users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'  # Este valor sale del <str:username> del urls
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        """ Add user's posts to context """
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        # Add posts to context
        context['posts'] = Post.objects.filter(user=user).order_by('-created')

        return context
