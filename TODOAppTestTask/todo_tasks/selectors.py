from todo_tasks.models import TODOTask


def get_todo_tasks(author):
    return TODOTask.objects.filter(author=author)
