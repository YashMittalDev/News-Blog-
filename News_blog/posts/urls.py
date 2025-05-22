from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name="posts_home"),
    path('greet/',views.greet,name="greet") , #for optional query parameters.
    path(f'show/',views.show_post,name="show"),
    path(f'show/<int:post_id>',views.show_one_post,name="show"),
    path('index/',views.index,name="index"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('create_post/',views.create_post,name='create_post'),
    path("post_one/<int:post_id>",views.post_one,name="post_one"),
    path("update/<int:post_id>",views.update,name="update")
]