from django.shortcuts import render

from blog.models import Post, Categories

# Create your views here.

def blog(request):
    posts = Post.objects.all()
    return render(request, "blog/blog.html", {"posts": posts})

def category(request, categories_id):
    categorie = Categories.objects.get(id=categories_id)
    posts = Post.objects.filter(category=categorie)
    return render(request, "blog/categories.html", {'categorie': categorie, "posts": posts})