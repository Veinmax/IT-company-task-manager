from django.test import TestCase
from django.contrib.auth import get_user_model
from task_manager.models import Position, TaskType, Task


class ModelsTests(TestCase):
    def test_position_str(self):
        position = Position.objects.create(
            name="Test name",
        )
        self.assertEqual(
            str(position),
            position.name
        )

    def test_task_type_str(self):
        task_type = TaskType.objects.create(
            name="Test name",
        )
        self.assertEqual(
            str(task_type),
            task_type.name
        )

    def test_create_worker_with_position(self):
        username = "Test name"
        password = "test1234"
        position = Position.objects.create(
            name="Test position name",
        )
        worker = get_user_model().objects.create_user(
            username=username,
            password=password,
            position=position
        )
        self.assertEqual(worker.username, username)
        self.assertTrue(worker.check_password(password))
        self.assertEqual(worker.position, position)
        self.assertEqual(
            str(worker),
            f"{worker.first_name} {worker.last_name}"
        )

    def test_task(self):
        task_type = TaskType.objects.create(
            name="Test name",
        )
        worker = get_user_model().objects.create_user(
            username="Test user name",
        )
        description = "Test description text with several words"
        deadline = "2023-11-23"
        priority = "Low"
        task = Task.objects.create(
            name="Test task name",
            description=description,
            deadline=deadline,
            is_completed=True,
            priority=priority,
            task_type=task_type
        )
        worker.tasks.add(task)
        self.assertEqual(
            str(task),
            task.name
        )
        self.assertTrue(
            task.assignees.filter(username=worker.username).exists()
        )
        self.assertEqual(
            task.task_type.name,
            task_type.name
        )
        self.assertEqual(
            task.description,
            description
        )
        self.assertEqual(
            task.deadline,
            deadline
        )
        self.assertEqual(
            task.priority,
            priority
        )
