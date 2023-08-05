from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import TaskList
from .serializers import TaskListSerializer

class TaskList(GenericAPIView):
    serializer_class = TaskListSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        task_list = serializer.save(user=self.request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
