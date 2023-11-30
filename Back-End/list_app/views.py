from django.shortcuts import render, get_object_or_404
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST,HTTP_201_CREATED
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ListAllSerializer, TaskAllSerializer, SubTaskSerializer
from .models import List, Task, SubTask
import requests
from requests_oauthlib import OAuth1


class All_list(APIView):
    def get(self, request):
        lists = List.objects.all()
        serialized_lists = ListAllSerializer(lists, many=True)
        return Response(serialized_lists.data)
    
    def post(self, request):
        new_list = ListAllSerializer(data=request.data)
        if new_list.is_valid():
            new_list.save()
            return Response(new_list.data, status=HTTP_201_CREATED)
        else:
            return Response(new_list.errors, status=HTTP_400_BAD_REQUEST)


class A_list(APIView):
    def get(self, request, id):

        alist = get_object_or_404(List, id = id)
        return Response(ListAllSerializer(alist).data)

        # print("hi")
        # alist = ListAllSerializer(List.objects.get(id=id))
        # print(alist)
        # return Response(alist.data)

    def put(self, request, id):
        list = List.objects.get(id=id)
        ser_list = ListAllSerializer(list, data=request.data, partial=True)
        if ser_list.is_valid():
            ser_list.save()
            return Response(status=HTTP_204_NO_CONTENT)
        else:
            return Response(status=HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        list = List.objects.get(id=id)
        list.delete()
        return Response(status=HTTP_204_NO_CONTENT)



class All_list_tasks(APIView):
    def get(self, request, id):
        tasks = TaskAllSerializer(Task.objects.filter(parent_list=id), many=True)
        return Response(tasks.data)
    
    def post(self, request, id):
        new_task = TaskAllSerializer(data=request.data)
        if new_task.is_valid():
            new_task.save()
            return Response(new_task.data, status=HTTP_201_CREATED)
        else:
            return Response(new_task.errors, status=HTTP_400_BAD_REQUEST)

class A_list_task(APIView):
    def get(self, request, id, task_id):
        task = TaskAllSerializer(Task.objects.get(id=task_id))
        return Response(task.data)

    def put(self, request, id, task_id):
        task = Task.objects.get(id=task_id)
        ser_task = TaskAllSerializer(task, data=request.data, partial=True)
        if ser_task.is_valid():
            ser_task.save()
            return Response(status=HTTP_204_NO_CONTENT)
        else:
            return Response(status=HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, task_id):
        task = Task.objects.get(id=task_id)
        task.delete()
        return Response(status=HTTP_204_NO_CONTENT)
        

class All_list_subtasks(APIView):
    def get(self, request, task_id):
        subtasks = SubTaskSerializer(SubTask.objects.filter(parentTask=task_id), many=True)
        return Response(subtasks.data)

    def post(self, request):
        new_subtask = SubTaskSerializer(data=request.data)
        if new_subtask.is_valid():
            new_subtask.save()
            return Response(new_subtask.data, status=HTTP_201_CREATED)
        else:
            return Response(new_subtask.errors, status=HTTP_400_BAD_REQUEST)

class A_list_subtask(APIView):
    def get(self, request, subtask_id): 
        subtask = SubTaskSerializer(SubTask.objects.get(id=subtask_id))       
        return Response(subtask.data)

    def put(self, request, subtask_id):
        subtask = SubTask.objects.get(id=subtask_id)
        ser_subtask = SubTaskSerializer(subtask, data=request.data, partial=True)
        if ser_subtask.is_valid():
            ser_subtask.save()
            return Response(status=HTTP_204_NO_CONTENT)
        else:
            return Response(status=HTTP_400_BAD_REQUEST)
    
    def delete(self, request, subtask_id):
        subtask = SubTask.objects.get(id=subtask_id)
        subtask.delete()
        return Response(status=HTTP_204_NO_CONTENT)