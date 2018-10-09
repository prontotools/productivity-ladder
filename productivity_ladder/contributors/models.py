from django.db import models


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
