# Generated by Django 3.0.5 on 2020-04-10 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memo_card', '0003_memocard'),
    ]

    operations = [
        migrations.AddField(
            model_name='memocard',
            name='pl_bold',
            field=models.TextField(blank=True, null=True),
        ),
    ]
