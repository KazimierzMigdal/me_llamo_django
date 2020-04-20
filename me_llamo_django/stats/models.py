from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.urls import reverse


class Statistic(models.Model):
    day = models.DateField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_statistics')
    right = models.IntegerField(default=0)
    wrong = models.IntegerField(default=0)
    near = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} stats, day: {self.day}'
