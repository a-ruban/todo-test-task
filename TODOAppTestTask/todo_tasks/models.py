import uuid

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models


class TODOTask(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    author = models.ForeignKey(to=get_user_model(), related_name='created_tasks', on_delete=models.CASCADE)
    title = models.CharField(max_length=settings.TODO_TASK_MAX_TITLE_LENGTH, blank=False)
    content = models.CharField(max_length=settings.TODO_TASK_MAX_CONTENT_LENGTH, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # for future usage
