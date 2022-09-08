from django.urls import include, path

from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('teachers', views.teachers, name='teachers'),
    path('availability/<int:teacherid>', views.setAvailability, name='availability'),
    path('addTeacher', views.addTeacher, name='addTeacher'),
    path('addTeacher/<int:id>', views.addTeacher, name='addTeacher'),
    path('login', auth_views.LoginView.as_view(template_name = 'registration/login.html'), name = 'login'),
    path('logout', auth_views.LogoutView.as_view(template_name = 'logout.html'), name = 'logout'),
    path('register', views.register, name = 'register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('activate/<uidb64>/<token>', views.activate, name='activate')
]