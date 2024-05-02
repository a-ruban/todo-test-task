from django.urls import path

from todo_tasks.views import TODOTaskListCreateView

urlpatterns = [
    path('', TODOTaskListCreateView.as_view(), name='task_list_create'),
]
