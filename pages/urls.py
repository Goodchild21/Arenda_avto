from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='pages-home'),
    path('about/', views.about, name='pages-about'),
    path('conditions/', views.conditions, name='pages-conditions'),
    path('contacts/', views.contacts, name='pages-contacts'),
]