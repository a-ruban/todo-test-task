from todo_tasks.models import TODOTask


class TODOTaskService:
    @staticmethod
    def create_task(author, title, content):
        return TODOTask.objects.create(author=author, title=title, content=content)
