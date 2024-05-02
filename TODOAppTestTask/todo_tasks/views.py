from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from todo_tasks.selectors import get_todo_tasks
from todo_tasks.serializers import InterviewTranscriptSerializer
from todo_tasks.services import TODOTaskService


class TODOTaskListCreateView(APIView):
    permission_classes = (IsAuthenticated, )
    InputSerializer = InterviewTranscriptSerializer
    OutputSerializer = InterviewTranscriptSerializer

    def post(self, request, *args, **kwargs):
        input_data = request.data | {'author': request.user.id}
        serializer = self.InputSerializer(data=input_data)
        serializer.is_valid(raise_exception=True)

        task = TODOTaskService.create_task(
            **serializer.validated_data
        )
        response_data = self.OutputSerializer(instance=task).data
        return Response(data=response_data, status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        todo_tasks = get_todo_tasks(
            author=request.user
        )
        data = self.OutputSerializer(todo_tasks, many=True).data
        return Response(data, status=status.HTTP_200_OK)
