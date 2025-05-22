from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest
from .forms import PostCreationForm
from .models import Post
from django.contrib.auth.decorators import login_required

# Create your views here.

def greet(request:HttpRequest):
    name = request.GET.get("name") or "World"
    return HttpResponse(f"Hello {name}")

# posts = [
#     {
#         'id':1,
#         'title':'Yash Mittal',
#         'description':'BCA'
#     },
#     {
#         'id':2,
#         'title':'Amit Mittal',
#         'description':'BCA'
#     },
#     {
#         'id':3,
#         'title':'ankit sharma',
#         'description':'BCA'
#     }
# ] git commit -m "Form creation without importing Models filw"

def show_post(request:HttpRequest):
    return HttpResponse(str(posts))

def show_one_post(request:HttpRequest,post_id):
    for post in posts:
        if post['id'] == post_id:
            return HttpResponse(str(post))
    return HttpResponse("Not Found")

def index(request:HttpRequest):
    name="yash"
    context = { "name":name}
    return render(request,"index.html",context)

def home(request:HttpRequest):
    posts = Post.objects.all()
    context = {"posts":posts}
    return render(request,"home.html",context)

def about(request:HttpRequest):
    context = {}
    return render(request,"about.html",context)

def contact(request:HttpRequest):
    context = {}
    return render(request,"contact.html",context)

@login_required
def create_post(request:HttpRequest):
    '''
    form = PostCreationForm()
    if request.method == "POST":
        title = request.POST['title']    
        author = request.POST['author']
        description = request.POST['description']
        new_post = Post(title=title,author=author,description=description)
        new_post.save()
        return redirect("posts_home")
    --this is when we create form without taking help of models and with models we do this.
    '''

    form = PostCreationForm()
    if request.method == "POST":
        form = PostCreationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("posts_home")
    context = {
        "form":form
    }
    return render(request,'create_post.html',context)


def post_one(request:HttpRequest,post_id):
    post = Post.objects.get(pk=post_id)
    if post:
        context = {"post":post}
    else:
        context={}
    return render(request,"post_one.html",context)

@login_required
def update(request:HttpRequest,post_id):
    post = Post.objects.get(pk=post_id)
    form = PostCreationForm(instance=post)
    if request.method == "POST":
        form = PostCreationForm(instance=post,data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts_home')
    context={'form':form}
    return render(request,"update.html",context)