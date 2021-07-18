# Django
import posts
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

# Forms
from posts.forms import PostForm

# Models
from posts.models import Post


# Con este decorador permitimos acceder a esta vista
# solo si esta logeado
# @login_required
# def list_posts(request):
#     """ Lista de posts existentes """
#     # Buscamos todos los post y los ordenamos por la fecha de
#     # creación (al tener el - significa en sentido inverso)
#     posts = Post.objects.all().order_by('-created')
#     return render(request, 'posts/feed.html', {'posts': posts})

@login_required
def create_post(request):
    """ Create new post view. """
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:feed')
    else:
        form = PostForm()
    
    return render(
        request=request,
        template_name='posts/new.html',
        context={
            'form': form,
            'user': request.user,
            'profile': request.user.profile
        }
    )
        
class PostFeedView(LoginRequiredMixin, ListView):
     """ Return all published posts. """

     template_name = 'posts/feed.html'
     model = Post
     ordering = ('-created')
     paginate_by = 2
     context_object_name = 'posts'
