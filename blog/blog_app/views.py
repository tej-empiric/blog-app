from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Blog
from .forms import BlogForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


@login_required
def create_blog(request):
    try:
        if request.method == "POST":
            form = BlogForm(request.POST)
            if form.is_valid():
                blog = form.save(commit=False)
                blog.user = request.user
                blog.save()
                return redirect("/", pk=blog.pk)
        else:
            form = BlogForm()
    except Exception as e:
        print("Error creating blog")

    return render(request, "blog/create_blog.html", {"form": form})


@login_required
def blog(request, id):
    try:
        blog = Blog.objects.get(pk=id)
    except Exception as e:
        print("Error displaying blog")

    return render(request, "blog/blog.html", {"blog": blog})


def edit(request, id):
    blog = get_object_or_404(Blog, pk=id)

    if request.method == "POST":
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, "Blog updated successfully")
            return render(request, "blog/blog.html", {"blog": blog})
        else:
            form = BlogForm(instance=blog)

    context = {"form": form}
    return render(request, "blog/edit.html", context)


def delete(request, id):
    blog = Blog.objects.get(pk=id)
    blog.delete()
    return HttpResponseRedirect(reverse("iframe"))


@login_required
def iframe(request):
    return render(request, "blog/iframe.html")
