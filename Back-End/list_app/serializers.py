from rest_framework import serializers
from .models import List, Task,SubTask
# from user_app.serializers import UserSerializer



class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = "__all__"

class TaskAllSerializer(serializers.ModelSerializer):
    subtasks = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = [
            "task_name",
            "completed",
            "task_description",
            "subtasks",
        ]

    def get_subtasks(self, instance):
        subtasks = instance.subtasks.all()
        subtask_names = [subtask.subtask_name for subtask in subtasks]
        return subtask_names

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model= Task
        fields= "__all__"

class ListAllSerializer(serializers.ModelSerializer):
    tasks = serializers.SerializerMethodField()

    class Meta:
        model = List
        fields = [
            "list_name",
            # "user",
            "completed",
            "tasks",
        ]

    def get_tasks(self, instance):
        tasks = instance.tasks.all()
        task_names = [task.task_name for task in tasks]
        return task_names

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = "__all__"