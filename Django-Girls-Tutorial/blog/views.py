from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)
from blog.models import Post
from django.utils import timezone
from blog.forms import PostForm

def post_list(request):
    # _이 아니라 __(2개)를 작성하셔야합니다.
    # order_by는 기본적으로 작은 것 > 큰 것 (여기서는 오래된 글 > 최신 글)로 되어있습니다. 이를 반대로 바꾸시려면 아래와 같이 - 를 붙여주시면 됩니다.
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})

def post_new(request):
    print(request.method)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.author = request.user
            post.publish()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form':form}) 

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid:
            post = form.save(commit=False)
            post.author = request.user
            post.publish()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form':form}) 

