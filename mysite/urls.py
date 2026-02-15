from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [

    path('admin/', admin.site.urls),

    path('', views.index, name='home'),

    path('projects/', views.projects, name='projects'),
    path('projects/create/', views.create_project, name='create_project'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('project/<int:pk>/edit/', views.edit_project, name='edit_project'),
    path('project/<int:pk>/delete/', views.delete_project, name='delete_project'),
    path('register/', views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', views.login_view, name='login'),
]