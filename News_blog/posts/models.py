from django.db import models

# Create your models here.

'''
class Post(models.Model):
    title : str
    description: str
    author: str
    image : image
    published_date : date
'''

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=50)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to="thumbnail/",default="default.png")
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

'''
notes:- 
from posts.models import Post 
new_post = Post(title="Python Tutorials",author="Yash mittal",description="python complete abc") 
new_post.save() #to save in db
new_post.title # python tutorials

to get all rows from the database:- 
 Post.objects.all()
<QuerySet [<Post: Post object (1)>, <Post: Post object (2)>]>

#to change the post object (1) and get a good name for row we use:- 

def __str__(self):
    return self.title

Post.objects.all()
<QuerySet [<Post: Python Tutorials>, <Post: Django>]>


#searching
 Post.objects.filter(title="Python Tutorials").all()
<QuerySet [<Post: Python Tutorials>]>

#search and get one
Post.objects.filter(title="Python Tutorials").first()
<Post: Python Tutorials>

'''
