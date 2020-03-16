from django.shortcuts import render, redirect
from .models import Blog

def index(request):
    return render(request, 'index.html')


# SHow all the blogs

def blogs(request):
    blogs = Blog.objects.all()
    context = {
        'all_blog' : blogs
    }
    return render(request, 'blogs.html', context)


# Write a new blog

def write(request):
    if request.method == 'GET':
        return render(request, 'write.html')

    elif request.method == 'POST':
        bname = request.POST["bname"]
        body = request.POST["body"]
        blog = Blog(title= bname, content= body)
        blog.save()

        return redirect('/blogs')


# Edit the created blog

def edit(request,id):
    blog = Blog.objects.get(id=id)
    context = {
        'edit_blog' : blog
    }

    if request.method == "GET":
        return render(request, "edit.html", context)

    elif request.method == "POST":
        bname = request.POST["bname"]
        body = request.POST["body"]
        blog = Blog(title= bname, content= body)
        blog.save()

        return redirect('/blogs')


# Delete the created blog

def delete(request, id):
    blog = Blog.objects.get(id=id)

    context = {
        'delete_blog' : blog
    }

    if request.method == "GET":
        return render(request, "delete.html", context)

    elif request.method == "POST":
        blog.delete()

        return redirect("/blogs")