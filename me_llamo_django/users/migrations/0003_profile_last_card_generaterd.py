# Generated by Django 3.0.5 on 2020-04-10 10:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_new_card_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='last_card_generaterd',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
