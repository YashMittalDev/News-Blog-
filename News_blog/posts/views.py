from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
# Create your views here.




def greet(request:HttpRequest):
    name = request.GET.get("name") or "World"
    return HttpResponse(f"Hello {name}")

posts = [
    {
        'id':1,
        'title':'Yash Mittal',
        'description':'BCA'
    },
    {
        'id':2,
        'title':'Amit Mittal',
        'description':'BCA'
    },
    {
        'id':3,
        'title':'ankit sharma',
        'description':'BCA'
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