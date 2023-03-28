from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import InsertForm,CategoryForm
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# ORM 
# Create your views here.

def index(r):
    data = {
        "categories":Category.objects.all(),
        "posts" :Post.objects.all()
    }
    return render(r,"home.html",data)

def filter(r,cat_id):
    data = {
        "categories":Category.objects.all(),
        "posts":Post.objects.filter(category__id=cat_id)
    }
    return render(r,"home.html",data)

def search(r):
    search_data = r.GET.get("search","")
    data = {
        "categories":Category.objects.all(),
        "posts":Post.objects.filter(title__icontains=search_data)
    }
    return render(r,"home.html",data)

@login_required()
def insertPost(r):
    form = InsertForm(r.POST or None,r.FILES or None)
    data = {
        "form" :form,
        "categoryForm":CategoryForm
    }

    if r.method == "POST":
        if form.is_valid():
            p = form.save(commit=False)
            p.author = r.user
            p.save()
            return redirect(index)
    return render(r,"insert.html",data)

@login_required()
def insertCategory(r):
    form = CategoryForm(r.POST or None)
    
    if r.method == "POST":
        if form.is_valid():
           form.save()
           return redirect(insertPost)
        

def viewPost(r,id):
    singlePost = get_object_or_404(Post,pk=id)
    data = {
        "categories":Category.objects.all(),
        "post" : singlePost ,
        "related_post" : Post.objects.filter(~Q(pk=id) & Q(category__id=singlePost.category.id))
    }
    return render(r, "details.html",data)

def deletePost(r,id):
    pass 

def register(r):
    form = UserCreationForm(r.POST or None)

    if r.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("signin")
    return render(r,"register.html",{"form":form})


def signin(r):
    form = AuthenticationForm(r.POST or None)

    if r.method == "POST":
        username = r.POST.get("username")
        password = r.POST.get("password")

        user  = authenticate(username=username,password=password)

        if user is not None:
            login(r,user)
            back = r.GET.get("next","/")
            return redirect(back)
            
        
    return render(r,"login.html",{"form":form})

@login_required()
def signout(r):
    logout(r)
    return redirect(index)
