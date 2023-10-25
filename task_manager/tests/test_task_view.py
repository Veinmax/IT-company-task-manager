from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from task_manager.models import Task, TaskType

TASK_LIST_URL = reverse("task_manager:task-list")


class PublicTaskTest(TestCase):
    def test_login_required(self):
        res = self.client.get(TASK_LIST_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateManufacturerTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create(
            username="test",
            password="test1234"
        )
        self.client.force_login(self.user)

    def test_retrieve_task(self):
        task_type = TaskType.objects.create(name="test type")
        Task.objects.create(
            name="test1",
            deadline="2023-10-10",
            task_type=task_type
        )
        Task.objects.create(
            name="test2",
            deadline="2023-10-10",
            task_type=task_type
        )
        response = self.client.get(TASK_LIST_URL)
        self.assertEqual(response.status_code, 200)
        tasks = Task.objects.all()
        self.assertEqual(
            list(response.context["task_list"]),
            list(tasks)
        )
        self.assertTemplateUsed(response, "task_manager/task_list.html")
        self.assertTrue(
            response.context.get("search_form"),
        )
        response = self.client.get(
            TASK_LIST_URL,
            data={"name": "test1"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["task_list"]), 1)
