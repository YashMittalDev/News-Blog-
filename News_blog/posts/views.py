from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
# Create your views here.




def greet(request:HttpRequest):
    name = request.GET.get("name") or "World"
    return HttpResponse(f"Hello {name}")

posts = [
    {
        'id':1,
        'name':'Yash Mittal',
        'class':'BCA'
    },
    {
        'id':2,
        'name':'Amit Mittal',
        'class':'BCA'
    },
    {
        'id':3,
        'name':'ankit sharma',
        'class':'BCA'
    }
]
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
    context = {"posts":posts}
    return render(request,"home.html",context)

def about(request:HttpRequest):
    context = {"posts":posts}
    return render(request,"about.html",context)

def contact(request:HttpRequest):
    context = {"posts":posts}
    return render(request,"contact.html",context)