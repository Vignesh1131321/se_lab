tasks = []

def add_task(title):
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "completed": False
    }
    tasks.append(task)
    return task

def list_tasks():
    return tasks

def update_task(task_id, completed=None, title=None):
    for task in tasks:
        if task["id"] == task_id:
            if title is not None:
                task["title"] = title
            if completed is not None:
                task["completed"] = completed
            return task
    return None

def delete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return True
    return False