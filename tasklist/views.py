from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import TaskList
from .serializers import TaskListSerializer, TaskListUpdateSerializer

class TaskListView(GenericAPIView):
    serializer_class = TaskListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        task_list_id = self.kwargs.get('task_list_id')
        if task_list_id is not None:
            return TaskList.objects.filter(id=task_list_id, user=self.request.user)
        else:
            return TaskList.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return TaskListUpdateSerializer  # Use the update serializer for PUT
        return TaskListSerializer

    def get(self, request, task_list_id=None):  # Accept the task_list_id parameter
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, task_list_id):
        TaskList.objects.filter(id=task_list_id).delete()
        return Response({"message":"deleted successfuly"})

    def put(self, request, task_list_id):
        task_list = get_object_or_404(TaskList, id=task_list_id, user=self.request.user)
        serializer = self.get_serializer(task_list, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Updated successfully"})
