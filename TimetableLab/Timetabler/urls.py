from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('teachers', views.teachers, name='teachers'),
    path('availability/<int:teacherid>', views.setAvailability, name='availability'),
    path('addTeacher', views.addTeacher, name='addTeacher'),
    path('addTeacher/<int:id>', views.addTeacher, name='addTeacher'),
]