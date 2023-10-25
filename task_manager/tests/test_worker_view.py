from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from task_manager.models import Worker, Position

WORKER_LIST_URL = reverse("task_manager:worker-list")


class PublicWorkerTest(TestCase):
    def test_login_required(self):
        response = self.client.get(WORKER_LIST_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivateWorkerTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create(
            username="test",
            password="test1234"
        )
        self.client.force_login(self.user)

    def test_retrieve_worker(self):
        response = self.client.get(WORKER_LIST_URL)

        self.assertEqual(response.status_code, 200)
        workers = Worker.objects.all()
        self.assertEqual(
            list(response.context["worker_list"]),
            list(workers)
        )
        self.assertTemplateUsed(response, "task_manager/worker_list.html")

    def test_create_worker(self):
        position = Position.objects.create(
            name="test position"
        )
        form_data = {
            "username": "new_user",
            "position": 1,
            "password1": "user12test",
            "password2": "user12test",
            "first_name": "Test first",
            "last_name": "Test last"
        }
        self.client.post(reverse("task_manager:worker-create"), data=form_data)
        new_user = get_user_model().objects.get(username=form_data["username"])

        self.assertEqual(new_user.position, position)
        self.assertEqual(new_user.first_name, form_data["first_name"])
        self.assertEqual(new_user.last_name, form_data["last_name"])
