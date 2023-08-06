from django.shortcuts import render
from . serializers import TasksViewSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import GenericAPIView
# Create your views here.

class TasksView(GenericAPIView):

    serializer_class = TasksViewSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        task = serializer.save()
        response_data = {
            "tasks": {
                "id": task.id,
                "name": task.name,
                "task_list": task.task_list.name
            }
        }
        return Response(response_data, status=status.HTTP_201_CREATED)