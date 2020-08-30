from django.shortcuts import render
from rest_framework import viewsets
from todobucket.models import Bucket, Todo
from todobucket.api.serializers import BucketSerializer, TodoSerializer


class BucketViewSet(viewsets.ModelViewSet):
    queryset = Bucket.objects.all()
    serializer_class = BucketSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
