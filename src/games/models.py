from django.db import models


class Game(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return f"Game: {self.name}"
