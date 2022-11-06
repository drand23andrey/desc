from django.urls import path

from . import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='task_list'),
    path('create_task/', views.CreateTaskView.as_view(), name='create_task'),
    path('task/<int:id>/', views.TaskView.as_view(), name='task'),
]