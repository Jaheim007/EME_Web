from django.urls import path 
from Front.views import index,about,contact,sermon

urlpatterns = [
    path('', index , name="home"),
    path('about/', about , name="about"),
    path('contact/', contact , name="contact"),
    path('sermon/', sermon , name="sermon"),
]
