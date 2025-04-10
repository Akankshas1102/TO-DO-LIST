# Not using Django ORM since Supabase is handling data
from django.db import models

# Dummy model in case it's ever needed
class Dummy(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
