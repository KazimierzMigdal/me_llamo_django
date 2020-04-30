from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q
from django.utils import timezone
from django.urls import reverse
import datetime


class StatisticMenager(models.Manager):
    def get_user_statistics(self, user):
        days = []
        day_right = []
        day_wrong = []
        day_near = []
        week_right = 0
        week_wrong = 0
        week_near = 0
        for days_ago in range(0,7):
            day = datetime.date.today() -  datetime.timedelta(days=days_ago)
            days.append(day)
            try:
                stats = Statistic.objects.get(Q(user=user)&Q(day=day))
                week_right = week_right + stats.right
                week_wrong = week_wrong + stats.wrong
                week_near = week_near + stats.near
                day_right.append(stats.right)
                day_wrong.append(stats.wrong)
                day_near.append(stats.near)
            except:
                day_right.append(0)
                day_wrong.append(0)
                day_near.append(0)

        return {'week_right': week_right,
            'week_wrong': week_wrong,
            'week_near' : week_near,
            'days':days,
            'day_right':day_right,
            'day_wrong':day_wrong,
            'day_near':day_near
            }


class Statistic(models.Model):
    day = models.DateField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_statistics')
    right = models.IntegerField(default=0)
    wrong = models.IntegerField(default=0)
    near = models.IntegerField(default=0)

    objects = StatisticMenager()

    def __str__(self):
        return f'{self.user.username} stats, day: {self.day}'
