from django.urls import path
from . import views
urlpatterns = [
    path('login/',views.logIn,name="login"),
        path('log_out/',views.log_out,name="log_out"),
            path('sign_up/',views.sign_up,name="sign_up"),
]