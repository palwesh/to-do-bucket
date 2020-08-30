from rest_framework import serializers
from todobucket.models import Bucket, Todo


class BucketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bucket
        fields = ('id', 'title', 'description', 'created_at', 'updated_at')


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'todo_task', 'status', 'bucket', 'created_at')
