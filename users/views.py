""" Users views. """
# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, FormView, UpdateView
from django.urls import reverse, reverse_lazy

# Models
from django.contrib.auth.models import User
from users.models import Profile

# Forms
from posts.models import Post
from users.forms import SignupForm


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


class SignupView(FormView):
    """ Users sign up view """
    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """ Save form data. """
        form.save()
        return super().form_valid(form)


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """ Update profile view. """
    template_name = 'users/update_profile.html'
    model = Profile
    fields = ['website', 'biography', 'phone_number', 'picture']

    def get_object(self, queryset=None):
        """ Return user's profile. """
        return self.request.user.profile

    def get_success_url(self):
        """ Return to user's profile. """
        username = self.object.user.username
        return reverse('users:detail', kwargs={
            'username': username
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
