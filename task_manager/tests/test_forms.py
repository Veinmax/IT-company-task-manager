from django.test import TestCase
from task_manager.forms import WorkerCreationForm
from task_manager.models import Position


class TestForm(TestCase):
    def test_worker_creation_form(self):
        position = Position.objects.create(
            name="test position"
        )
        form_data = {
            "username": "new_user",
            "password1": "user12test",
            "password2": "user12test",
            "position": position,
            "first_name": "Test first",
            "last_name": "Test last"
        }
        form = WorkerCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)
