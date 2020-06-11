from django.shortcuts import render, get_object_or_404, redirect
from . models import Post
from . forms import PostForm
from django.core.paginator import Paginator



def index(request):
        post_list = Post.objects.order_by("-pub_date").all()
        paginator = Paginator(post_list, 2)
        page_number = request.GET.get('page')
        page = paginator.get_page(page_number)
        return render(request, 'index.html', {'page': page, 'paginator': paginator})


def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST or None, files=request.FILES or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('index')
        return render(request, 'new_post.html', {'form': form})
    form = PostForm()
    return render(request, 'new_post.html', {'form': form})


def post_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    count = Post.objects.count()


    return render(
        request,
        "post.html",
        {
            'post': post,
            'count': count,
        }
    )


def post_edit(request, post_id):
        post = get_object_or_404(Post, id=post_id)
        form = PostForm(request.POST or None, files=request.FILES or None, instance=post)

        if request.method == "POST":
            if form.is_valid():
                form.save()
                return redirect("post", post_id=post_id)

        return render(
                request, "post_edit.html", {"form": form, "post": post},
        )
