from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('servises.html', views.servises, name='servises'),
    path('blog.html', views.blogs, name='blogs'),
    path('contact.html', views.contacts, name='contacts'),

]