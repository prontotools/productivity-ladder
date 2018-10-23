from django.contrib.auth.models import User
from django.test import TestCase

from contributors.admin import CommitAdmin, ContributorAdmin


class TestContributorAdmin(TestCase):
    def setUp(self):
        username = 'admin'
        password = 'admin'
        email = 'admin@gmail.com'

        User.objects.create_superuser(username, password, email)
        self.client.login(username=username, password=password)

    def test_should_show_column_defined(self):
        expected = ('id', 'username', 'name')

        actual = ContributorAdmin.list_display
        self.assertEquals(actual,  expected)

    def test_should_accessible(self):
        response = self.client.get('/admin/contributors/contributor')

        self.assertEqual(response.status_code, 301)

    def test_should_search_by_username(self):
        expected = ('username',)

        actual = ContributorAdmin.search_fields
        self.assertEqual(actual, expected)

    def test_should_show_30_list_per_page(self):
        expected = 30

        actual = ContributorAdmin.list_per_page
        self.assertEqual(actual, expected)


class TestCommitAdmin(TestCase):
    def setUp(self):
        username = 'admin'
        password = 'admin'
        email = 'admin@gmail.com'

        User.objects.create_superuser(username, password, email)
        self.client.login(username=username, password=password)

    def test_should_show_column_defined(self):
        expected = ('repositories', 'contributors', 'count', 'date_committed')

        actual = CommitAdmin.list_display
        self.assertEqual(actual, expected)

    def test_should_accessible(self):
        response = self.client.get('/admin/contributors/commit')

        self.assertEqual(response.status_code, 301)

    def test_should_search_by_repositories_contributors_and_date(self):
        expected = ('repositories', 'contributors', 'date_committed')

        actual = CommitAdmin.search_fields
        self.assertEqual(actual, expected)

    def test_should_show_30_list_per_page(self):
        expected = 30

        actual = CommitAdmin.list_per_page
        self.assertEqual(actual, expected)
