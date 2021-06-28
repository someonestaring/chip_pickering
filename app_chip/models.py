from django.db import models
from django.utils import timezone

class Visitor(models.Model):
    email = models.EmailField(max_length=254)
    name = models.TextField(default='', max_length=56)
    desc = models.TextField(default='', max_length=256)
    visited_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.name}'
