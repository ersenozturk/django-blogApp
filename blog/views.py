from django.shortcuts import render, redirect, get_object_or_404

from .models import Posts, PostLike, PostComment, PostView

from .forms import PostForm, LikeForm, CommentForm

from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your views here.
def post_list(request):  # ok

    posts = Posts.objects.filter(status='publish')
    likeform = LikeForm()

    if request.method == 'POST':
        if 'like' in request.POST:
            if request.user.is_authenticated:
                # print('Like request', request.POST)
                user = User.objects.get(id=request.user.id)
                post = Posts.objects.get(slug=request.POST['slug'])
                # print(post)
                b1 = PostLike(user=user, posts=post)
                instance = PostLike.objects.filter(user=b1.user, posts=b1.posts)
                if instance:
                    instance.delete()
                    # likeform = LikeForm()
                    return redirect('home')
                else:
                    b1.save()
                    # likeform = LikeForm()
                    return redirect('home')
            else:
                return redirect('login')


    context = {
        'posts': posts,
        'likeform': likeform,
    }
    return render(request, 'post_list.html', context)


def about(request):
    return render(request, 'about.html')




def post_create(request): 
    if not request.user.is_authenticated:
        return redirect('login')

    form = PostForm()

    if(request.method == 'POST'):
        form = PostForm(request.POST, request.FILES)
        obj = form.save(commit=False)
        obj.user = User.objects.get(pk=request.user.id)

        if(form.is_valid()):
            form.save()
            return redirect('home')

    context = {
        'form': form,
    }
    return render(request, 'post_create.html', context)



def post_update(request, id): 
    if not request.user.is_authenticated:
        return redirect('login')

    post = Posts.objects.get(pk=id)
    form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form,
    }

    return render(request, 'post_update.html', context)




def post_delete(request, id):
    if not request.user.is_authenticated:
        return redirect('login')

    post = Posts.objects.get(pk=id)
    form = PostForm(instance=post)

    if request.method == 'POST':
        post.delete()
        return redirect('home')

    context = {
        'form': form,
    }

    return render(request, 'post_delete.html', context)




def post_detail(request, slug):
        
    post = Posts.objects.get(slug=slug)
    comments = PostComment.objects.filter(post=post.id)
    commentform = CommentForm()
    likeform = LikeForm()

    print(request.POST)

    # Post view increment
    if not 'like' in request.POST:
        if not 'comment' in request.POST:
            if request.user.is_authenticated:
                user = User.objects.get(pk=request.user.id)
                postview = PostView(posts=post, user=user)
                postview.save()
            else:
                postview= PostView(posts=post)
                postview.save()


    if request.method == 'POST':
        # if not authenticate dont show another codes
        if not request.user.is_authenticated:
            return redirect('login')

        # Like request
        if 'like' in request.POST:
            # print('Like request')
            user = User.objects.get(id=request.user.id)
            post = Posts.objects.get(slug=slug)
            b1 = PostLike(user=user, posts=post)
            instance = PostLike.objects.filter(user=b1.user, posts=b1.posts)
            if instance:
                instance.delete()
            else:
                b1.save()
        # comment request
        elif 'comment' in request.POST:
            print('comment request')
            form = CommentForm(request.POST)

            # Return an object without saving to the DB
            obj = form.save(commit=False)
            obj.user = User.objects.get(pk=request.user.id)
            obj.post = Posts.objects.get(slug=slug)

            if form.is_valid():
                form.save()
                form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'commentform': commentform,
        'likeform': likeform,
    }

    return render(request, 'post_detail.html', context)
