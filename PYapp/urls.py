from django.urls import path

from . import views
from. views import home

urlpatterns = (
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('schedule/', views.schedule, name='schedule'),
    path('blog/', views.blog, name='blog'),
    path('classes/', views.classes, name='classes'),
)