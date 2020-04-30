from .models import Statistic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView
import datetime


class StatisticView(LoginRequiredMixin, TemplateView):
    template_name = 'stats/statistics.html'

    def get_context_data(self, **kwargs):
        context = super(StatisticView, self).get_context_data(**kwargs)
        user = self.request.user
        context['statistic'] = Statistic.objects.get_user_statistics(user)
        return context
