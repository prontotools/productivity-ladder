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

    def __str__(self):
        return f'username {self.username}'

class Contributor(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=100, null=False, blank=False, unique=True)

    def __str__(self):
        return f'username {self.username}'

class Commit(models.Model):
    count = models.IntegerField()
    date_commited = models.DateTimeField()
    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE)
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)

    def __str__(self):
        return f'contributor {self.contributor} of {self.repository}'

    class Meta:
        unique_together = (('contributor', 'repository'))
