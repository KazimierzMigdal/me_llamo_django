# Generated by Django 3.0.5 on 2020-04-11 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memo_card', '0007_auto_20200411_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repeat',
            name='repeat_on',
            field=models.DateTimeField(),
        ),
    ]
