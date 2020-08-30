from django.db import models

# Create your models here.


class Bucket(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=300)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Todo(models.Model):
    todo_task = models.CharField(max_length=200)
    status = models.BooleanField(default=False)

    bucket = models.ForeignKey(Bucket, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.todo_task
