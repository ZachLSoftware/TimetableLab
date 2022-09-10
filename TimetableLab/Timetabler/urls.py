from django.urls import include, path

from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('teachers', views.teachers, name='teachers'),
    path('availability/<int:teacherid>', views.setAvailability, name='availability'),
    path('setModules/<int:year>', views.setModules, name='setModules'),
    path('modules', views.modules, name='modules'),
    path('addYear', views.addYear, name="addYear"),
    path('addTeacher', views.addTeacher, name='addTeacher'),
    path('addTeacher/<int:id>', views.addTeacher, name='addTeacher'),
    path('login', auth_views.LoginView.as_view(template_name = 'registration/login.html'), name = 'login'),
    path('logout', views.logout_view, name = 'logout'),
    path('register', views.register, name = 'register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('successPage', views.successPage, name="successPage"),
    path('activate/<uidb64>/<token>', views.activate, name='activate')
]