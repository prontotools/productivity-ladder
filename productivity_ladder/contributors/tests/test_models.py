from django.test import TestCase
from django.utils import timezone

from contributors.models import Commit, Contributor
from repositories.models import Repository


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

    def test_should_add_repository(self):
        repository = Repository()
        repository.name = 'repo name'
        repository.save()

        Commit.objects.create(
            repositories=repository,
            contributors=self.contributor,
            count=10,
            date_committed=timezone.now(),
        )

        actual = Contributor.objects.last()

        self.assertEqual(actual.repositories.get(id=1).name, 'repo name')


class TestCommit(TestCase):
    def setUp(self):
        self.repository = Repository.objects.create(name='repo name')
        self.contributor = Contributor.objects.create(
            name='pop',
            username='saowaluck',
        )

        self.commit = Commit.objects.create(
            repositories=self.repository,
            contributors=self.contributor,
            count=10,
            date_committed=timezone.now(),
        )

    def test_should_save_commit(self):
        actual = Commit.objects.last()

        self.assertEqual(actual.repositories, self.repository)
        self.assertEqual(actual.contributors, self.contributor)
        self.assertEqual(actual.count, 10)
        self.assertTrue(actual.date_committed)

    def test_should_show_str(self):
        actual = self.commit.__str__()

        expected = f'{self.contributor} commit {self.repository}'
        self.assertEqual(actual, expected)
