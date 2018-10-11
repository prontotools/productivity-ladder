from datetime import datetime
from django.db import IntegrityError
from django.test import TestCase

import pytz

from contributors.models import Contributor, Commit
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


class TestCommit(TestCase):
    def setUp(self):
        self.contributor = Contributor()
        self.contributor.username = 'gogam'
        self.contributor.name = 'Gam Jiratchanon'
        self.contributor.contributor_id = '1'
        self.contributor.save()

        self.repository = Repository()
        self.repository.name = 'simplesat'
        self.repository.save()

        self.commit = Commit()
        self.commit.count = 200
        self.commit.date_commited = datetime(2018, 9, 11, tzinfo=pytz.UTC)
        self.commit.contributor_id = 1
        self.commit.repository_id = 1
        self.commit.save()

    def test_should_save_commit(self):
        actual = Commit.objects.last()

        self.assertEqual(actual.count, 200)
        self.assertEqual(actual.contributor_id, 1)
        self.assertEqual(actual.repository_id, 1)
        self.assertEqual(
            actual.date_commited, datetime(2018, 9, 11, tzinfo=pytz.UTC)
        )

    def test_save_duplicate_commit_should_cannot_save(self):
        commit = Commit()
        commit.count = 300
        commit.date_commited = datetime(2018, 9, 12, tzinfo=pytz.UTC)
        commit.contributor_id = 1
        commit.repository_id = 1

        self.assertRaises(IntegrityError, commit.save)

    def test_should_show_str(self):
        expected = f'contributor {self.contributor} of {self.repository}'

        actual = self.commit.__str__()

        self.assertEqual(actual, expected)
