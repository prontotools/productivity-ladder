from django.db import models

from repositories.models import Repository


class Contributor(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        unique=True,
    )
    repositories = models.ManyToManyField(Repository, through='Commit')

    def __str__(self):
        return f'username {self.username}'


class Commit(models.Model):
    repositories = models.ForeignKey(Repository, on_delete=models.CASCADE)
    contributors = models.ForeignKey(Contributor, on_delete=models.CASCADE)
    count = models.IntegerField()
    date_committed = models.DateTimeField()

    def __str__(self):
        return f'{self.contributors} commit {self.repositories}'
