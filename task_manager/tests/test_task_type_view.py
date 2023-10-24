from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from task_manager.models import TaskType

TASK_TYPE_LIST_URL = reverse("task_manager:task-type-list")


class PublicTaskTypeTest(TestCase):
    def test_login_required(self):
        res = self.client.get(TASK_TYPE_LIST_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateTaskTypeTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create(
            username="test",
            password="test1234"
        )
        self.client.force_login(self.user)

    def test_retrieve_task_type(self):
        TaskType.objects.create(name="test type")
        response = self.client.get(TASK_TYPE_LIST_URL)
        self.assertEqual(response.status_code, 200)
        task_types = TaskType.objects.all()
        self.assertEqual(
            list(response.context["task_type_list"]),
            list(task_types)
        )
        self.assertTemplateUsed(response, "task_manager/task_type_list.html")
