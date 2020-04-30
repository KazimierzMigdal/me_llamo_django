from .models import Statistic
from django.db.models import Q
from django.shortcuts import render
import datetime


def statistics(request):
    user = request.user
    context = Statistic.objects.get_user_statistics(user)
    return render(request, 'stats/statistics.html', context)
