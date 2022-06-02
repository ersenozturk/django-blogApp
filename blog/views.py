from django.shortcuts import redirect, render
# from .forms import StudentForm

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from blog.forms import PostForm
from blog.models import Posts


def post_list(request):
    posts = Posts.objects.all()

    context = {
        "posts": posts
    }
    return render(request, "blog/post_list.html", context)


def createPost(request):
    form = PostForm()

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {
        "form" : form
    }
    return render(request, "blog/post_create.html", context)

# def createPost(request):
#     form = PostForm()
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')

#     context = {
#         'form': form
#     }
#     return render(request, 'blog/post_create.html', context)

# def createPost(request):
#     form = PostForm()
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             postImage = form.save()
#             if 'image' in request.FILES:
#                 postImage.image = request.FILES.get('image')
#                 postImage.save()
#             return redirect('home')

#     context = {
#         'form': form
#     }
#     return render(request, 'blog/post_create.html', context)



def post_update(request, id):
    post = Posts.objects.get(id=id)
    form = PostForm(instance=post)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("list")

    context = {
        "form": form
    }
    return render(request, "blog/post_update.html", context)


# def student_delete(request, id):
#     student = Student.objects.get(id=id)

#     if request.method == "POST":
#         student.delete()
#         return redirect("list")

#     context = {
#         "student" : student
#     }

#     return render(request, "fscohort/student_delete.html", context)


def post_detail(request, id):
    post = Posts.objects.get(id=id)
    context = {
        'post': post
    }
    return render(request, 'blog/post_detail.html', context)
