from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from task_manager.models import Position

POSITION_LIST_URL = reverse("task_manager:position-list")


class PublicPositionTest(TestCase):
    def test_login_required(self):
        res = self.client.get(POSITION_LIST_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivatePositionTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create(
            username="test",
            password="test1234"
        )
        self.client.force_login(self.user)

    def test_retrieve_position(self):
        Position.objects.create(name="test position")
        response = self.client.get(POSITION_LIST_URL)
        self.assertEqual(response.status_code, 200)
        positions = Position.objects.all()
        self.assertEqual(
            list(response.context["position_list"]),
            list(positions)
        )
        self.assertTemplateUsed(response, "task_manager/position_list.html")
