from django.urls import path
from . views import TaskListView

urlpatterns = [
    path('', TaskListView.as_view()),
    path('<int:task_list_id>/', TaskListView.as_view())
]