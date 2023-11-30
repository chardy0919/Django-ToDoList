from django.db import models
# from user_app.models import Person




class List(models.Model):
    list_name=models.CharField(null=False, blank= False)
    # user= models.ForeignKey(null=False, blank=False, on_delete=models.CASCADE, to= Person)
    completed = models.BooleanField(default=False)


class Task(models.Model):
    task_name=models.CharField(null=False, blank=False)
    completed=models.BooleanField(null=False, blank=False, default=False)
    parent_list=models.ForeignKey(List, on_delete=models.CASCADE, related_name="tasks")
    task_description=models.CharField(null=True, blank=True)


class SubTask(models.Model):
    subtask_name = models.CharField(null=False, blank=False)
    completed = models.BooleanField(default=False, null=False, blank=False)
    parentTask = models.ForeignKey(Task,on_delete=models.CASCADE, related_name="subtasks" )