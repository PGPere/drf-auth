from django.test import TestCase
from django.contrib.auth import get_user_model

from spice.models import Spice


class SpiceTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(
            username='Kim', password='@12345678')
        test_user.save()

        test_spice = Spice.objects.create(
            author=test_user, title="Nutmeg", body="Nutty and spicy")
        test_spice.save()

    def test_things_model(self):
        spice = Spice.objects.get(id=1)
        actual_author = str(spice.author)
        actual_title = str(spice.title)
        actual_body = str(spice.body)
        self.assertEqual(actual_author, "Kim")
        self.assertEqual(actual_title, "@12345678")
        self.assertEqual(actual_body, "Nutty and spicy")
