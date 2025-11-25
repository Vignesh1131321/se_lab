import app


def setup_function():
    # Reset the in-memory tasks before each test
    app.tasks.clear()


def test_add_and_list_tasks():
    t1 = app.add_task("Buy milk")
    assert t1["id"] == 1
    assert t1["title"] == "Buy milk"
    assert t1["completed"] is False

    t2 = app.add_task("Walk dog")
    assert t2["id"] == 2

    all_tasks = app.list_tasks()
    assert isinstance(all_tasks, list)
    assert len(all_tasks) == 2
    assert all_tasks[0]["title"] == "Buy milk"


def test_update_task():
    app.add_task("Task A")
    app.add_task("Task B")
    updated = app.update_task(1, completed=True, title="Task A updated")
    assert updated is not None
    assert updated["id"] == 1
    assert updated["completed"] is True
    assert updated["title"] == "Task A updated"

    # updating non-existent id returns None
    assert app.update_task(999, title="Nope") is None


def test_delete_task():
    app.add_task("To delete")
    app.add_task("Keep")
    # delete id 1
    ok = app.delete_task(1)
    assert ok is True
    tasks = app.list_tasks()
    assert len(tasks) == 1
    # deleting again returns False
    assert app.delete_task(1) is False
