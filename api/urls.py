from django.urls import path
from .views import *

urlpatterns = [
    path('', apiOverview),
    path('task-list/', taskList, name='task_list'),
    path('task-detail/<str:pk>/', taskDetail, name='task_detail'),
    path('task-create/', taskCreate, name='task_create'),
    path('task-update/<str:pk>/', taskUpdate, name='task_update'),
    path('task-delete/<str:pk>/', taskDelete, name='task_delete'),
]
