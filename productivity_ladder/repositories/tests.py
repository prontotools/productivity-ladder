from django.test import TestCase

from repositories.models import Repository


class TestRepository(TestCase):
    def setUp(self):
        self.repository = Repository()
        self.repository.name = 'simplesat'
        self.repository.save()

    def test_should_save_repository(self):
        actual = Repository.objects.last()
        self.assertEqual(actual.name, self.repository.name)

    def test_should_show_str(self):
        actual = self.repository.__str__()
        expected = f'repository {self.repository.name}'

        self.assertEqual(actual, expected)
