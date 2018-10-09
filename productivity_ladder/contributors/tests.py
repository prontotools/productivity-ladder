from django.test import TestCase

from contributors.models import Contributor


class TestContributor(TestCase):
    def setUp(self):
        self.contributor = Contributor()
        self.contributor.username = 'saowaluck'
        self.contributor.name = 'pop'
        self.contributor.save()

    def test_should_save_contributor(self):
        actual = Contributor.objects.last()

        self.assertEqual(actual.username, 'saowaluck')
        self.assertEqual(actual.name, 'pop')

    def test_should_show_str(self):
        actual = self.contributor.__str__()

        expected = f'username {self.contributor.username}'
        self.assertEqual(actual, expected)

