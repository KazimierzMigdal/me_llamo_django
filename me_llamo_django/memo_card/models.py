from django.db import models
from django.contrib.auth.models import User
from stats.models import Statistic
import datetime


class CardMenager(models.Manager):
    def new_card(self, user):
        user_memocard = Repeat.objects.filter(user_for=user)
        stats = Statistic(day=datetime.date.today(),
                            user=user)
        stats.save()
        for memocard in user_memocard:
            if datetime.date.today() - memocard.repeat_on >= datetime.timedelta(days=1):
                memocard.repeat_on = datetime.date.today()
                memocard.save()
        new_card_number = user.profile.new_card_number
        if user_memocard.count() == 0:
             last_user_memocard_index = 0
        else:
            last_user_memocard_index = user_memocard.count()

        for num in range(1, new_card_number+1):
            new_card_index = last_user_memocard_index+num
            memocard = MemoCard.objects.get(id=new_card_index)
            repeat = Repeat(user_for=user,
                            card =memocard,
                            repeat_on=datetime.date.today(),
                            counter=0)
            repeat.save()
        user.profile.last_card_generaterd = datetime.date.today()
        user.profile.save()


class CategoryMemoCard(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_category')
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True, max_length=200)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'pk': self.pk})


class MemoCard(models.Model):
    GRUP_CHOISE = [('Shop','Shop'),
                    ('Activity', 'Activity'),
                    ('Time','Time'),
                    ('Hospital','Hospital'),
                    ('Apparition','Apparition'),
                    ('Family', 'Family'),
                    ('Meeting','Meeting'),
                    ('Phone', 'Phone'),
                    ('Opinion', 'Opinion'),
                    ('Profesion', 'Profesion'),
                    ('Relation', 'Relation'),
                    ('Emotions', 'Emotions')]

    esp_title = models.CharField(max_length=200)
    esp_eg = models.TextField(null = True, blank=True)
    esp_bold=models.TextField(null = True, blank=True)
    pl_title = models.CharField(max_length=200)
    pl_eg = models.TextField(null = True, blank=True)
    grup = models.CharField(choices = GRUP_CHOISE, null=True, blank=True, max_length=20)
    pl_bold=models.TextField(null = True, blank=True)

    objects = CardMenager()

    def __str__(self):
        return self.esp_title


class Repeat(models.Model):
    user_for = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_memocard')
    card = models.ForeignKey(MemoCard, on_delete=models.CASCADE, related_name='for_users')
    repeat_on = models.DateField()
    counter = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.user_for.username} repeat "{self.card.esp_title}"'


class UserMemoCard(models.Model):
    category = models.ForeignKey(CategoryMemoCard, on_delete=models.CASCADE, related_name='memocard')
    title = models.CharField(max_length=150)
    eg = models.TextField(null = True, blank=True, max_length=250)
    reverse_title = models.CharField(max_length=150)
    reverse_eg = models.TextField(null = True, blank=True, max_length=250)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('memocard_detail', kwargs={'pk': self.pk})
