# Generated by Django 3.0.5 on 2020-04-10 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memo_card', '0005_repeat'),
    ]

    operations = [
        migrations.AddField(
            model_name='repeat',
            name='counter',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
