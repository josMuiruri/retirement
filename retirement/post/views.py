from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . models import Post

# Create your views here.
@login_required
def create_post(request):
    if request.method == 'Post':
        content = request.POST.get('content')
        Post.objects.create(user=request.user, content=content)
        return redirect('home')
    return render(request, 'posts/create_post.html')

def view_posts(request):
    post = Post.objects.all().order_by('create_at')
    return render(request, 'posts/view_post.html')
