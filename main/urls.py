from django.conf.urls import url
from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path('', views.index, name="index"),
    path('contact/', views.contact, name="contact"),
    path('about/', views.AboutListView.as_view(), name="about"),
    path('tiny/', views.tiny),
]