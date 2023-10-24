from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from task_manager.models import Position


class AdminPanelWorkerTests(TestCase):

    def setUp(self) -> None:
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="admin123"
        )
        self.client.force_login(self.admin_user)
        self.position = Position.objects.create(name="Test name")
        self.worker = get_user_model().objects.create_user(
            username="worker",
            password="worker123",
            position=self.position
        )

    def test_worker_list_display(self):
        url = reverse("admin:task_manager_worker_changelist")
        res = self.client.get(url)

        self.assertContains(res, self.worker.position)

    def test_worker_detail_list_display(self):
        url = reverse("admin:task_manager_worker_change", args=[self.worker.id])
        res = self.client.get(url)

        self.assertContains(res, self.worker.position)

    def test_additional_info_fields_in_worker_add(self):
        url = reverse("admin:task_manager_worker_add")
        response = self.client.get(url)

        self.assertContains(response, "position")
        self.assertContains(response, "Additional info")


class AdminPanelPositionTests(TestCase):
    def setUp(self) -> None:
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="admin123"
        )
        self.client.force_login(self.admin_user)

    def test_position_is_register_in_admin(self):
        url = reverse("admin:task_manager_position_changelist")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)


class AdminPanelTaskTypeTests(TestCase):
    def setUp(self) -> None:
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="admin123"
        )
        self.client.force_login(self.admin_user)

    def test_task_type_is_register_in_admin(self):
        url = reverse("admin:task_manager_tasktype_changelist")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)


class AdminPanelTaskTests(TestCase):
    def setUp(self) -> None:
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="admin123"
        )
        self.client.force_login(self.admin_user)

    def test_task_is_register_in_admin(self):
        url = reverse("admin:task_manager_task_changelist")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
