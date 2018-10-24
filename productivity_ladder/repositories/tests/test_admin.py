from django.contrib.auth.models import User
from django.test import TestCase

from ..admin import RepositoryAdmin


class TestRepositoryAdmin(TestCase):
    def setUp(self):
        username = 'admin'
        password = 'admin'
        email = 'admin@gmail.com'

        User.objects.create_superuser(username, password, email)
        self.client.login(username=username, password=password)

    def test_should_accessiable(self):
        response = self.client.get('/admin/repositories/repository')
        self.assertEqual(response.status_code, 301)

    def test_should_show_defined_columns(self):
        expected = ('name', )

        actual = RepositoryAdmin.list_display
        self.assertEqual(actual, expected)

    def test_should_search_by_name(self):
        expected = ('name',)

        actual = RepositoryAdmin.search_fields
        self.assertEqual(actual, expected)
