from rest_framework import serializers

from TODOAppTestTask.settings import TODO_TASK_MIN_TITLE_LENGTH, TODO_TASK_MAX_TITLE_LENGTH, \
    TODO_TASK_MAX_CONTENT_LENGTH, TODO_TASK_MIN_CONTENT_LENGTH
from todo_tasks.models import TODOTask


class InterviewTranscriptSerializer(serializers.ModelSerializer):
    title = serializers.CharField(min_length=TODO_TASK_MIN_TITLE_LENGTH, max_length=TODO_TASK_MAX_TITLE_LENGTH,
                                  allow_blank=False, allow_null=False)
    content = serializers.CharField(min_length=TODO_TASK_MIN_CONTENT_LENGTH, max_length=TODO_TASK_MAX_CONTENT_LENGTH,
                                    allow_blank=False, allow_null=False)

    class Meta:
        model = TODOTask
        fields = '__all__'
