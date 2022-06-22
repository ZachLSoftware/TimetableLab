from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('teachers', views.teachers, name='teachers'),
    path('availability', views.setAvailability, name='availability'),
]