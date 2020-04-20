from .models import Statistic
from django.db.models import Q
from django.shortcuts import render
import datetime


def statistics(request):
    user = request.user
    today = today = datetime.date.today()
    today_stats = Statistic.objects.get(Q(user=user)&Q(day=today))
    right = today_stats.right
    wrong = today_stats.wrong
    near = today_stats.near

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
    context = {'right':right,
            'wrong': wrong,
            'near':near,
            'week_right': week_right,
            'week_wrong': week_wrong,
            'week_near' : week_near,
            'days':days,
            'day_right':day_right,
            'day_wrong':day_wrong,
            'day_near':day_near
    }
    return render(request, 'stats/statistics.html', context)
