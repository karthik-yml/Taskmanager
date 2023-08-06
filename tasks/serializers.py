from rest_framework import serializers
from . models import Tasks
class TasksViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tasks
        fields='__all__'