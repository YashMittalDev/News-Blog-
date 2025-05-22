from django.contrib import admin
from .models import Post
# Register your models here.

#admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','author','published_date']
    list_filter = ['published_date']
'''
now to integrate the model with admin we need to do the follwoing steps.
first import the model here
1. from .models import Post
now , register the model with admin to get its access on admin panel
2. admin.site.register(Post)
now , check in the admin panel you got the access.
yes.

now to edit or modify the admin panel we have to do the following:- 
creat a class and inherits the ModelAdmin class of admin with a decorator which register the post model
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','author']
'''

