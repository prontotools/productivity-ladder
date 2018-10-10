from django.db import models


class Repository(models.Model):
    name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        unique=True,
    )

    def __str__(self):
        return f'repository {self.name}'
