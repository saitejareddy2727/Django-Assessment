from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import CommentForm

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.filter(parent__isnull=True).order_by('created_at')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            parent_id = request.POST.get('parent')
            parent = Comment.objects.get(id=parent_id) if parent_id else None
            Comment.objects.create(
                post=post,
                author=form.cleaned_data['author'],
                text=form.cleaned_data['text'],
                parent=parent
            )
            return redirect('comment/post_detail', post_id=post.id)
    else:
        form = CommentForm()
    return render(request, 'commect/post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form
    })
