from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name="about"),
    path('puppies/', views.puppies_index, name="puppies_index"),
    path('puppies/<int:pup_id>/', views.puppies_detail, name='puppies_detail'),
]