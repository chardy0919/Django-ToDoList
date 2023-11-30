from django.urls import path
from .views import All_list, A_list,All_list_tasks,A_list_task,All_list_subtasks,A_list_subtask

urlpatterns = [
    path("", All_list.as_view(), name='All_list'),
    path("<int:id>/", A_list.as_view(), name="A_list"),
    path("<int:id>/task/", All_list_tasks.as_view(), name="All_list_tasks"),
    path("<int:id>/task/<int:task_id>/", A_list_task.as_view(), name="A_list_task"),
    path("<int:id>/task/<int:task_id>/subtask/", All_list_subtasks.as_view(), name="All_list_task_subtasks"),
    path("<int:id>/task/<int:task_id>/subtask/<int:subtask_id>", A_list_subtask.as_view(), name="All_list_task_subtask"),
]
