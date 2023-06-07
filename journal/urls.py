from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),

    path('task', views.task, name='task'), 
    path('create-task', views.create_task, name='create-task'),
    path('filter-task',views.filter_task, name='filter-task'),
    
    path('upate-task/<str:pk>', views.update_task, name='update-task'),
    path('delete-task/<str:pk>', views.delete_task, name='delete-task'),
    path('register',views.register,name="register"),
    path('success',views.success,name="success"),

    path('my_login', views.my_login, name="my_login"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('user_logout', views.user_logout, name="user_logout"),
]