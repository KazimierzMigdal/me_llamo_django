# Generated by Django 3.0.5 on 2020-04-11 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memo_card', '0008_auto_20200411_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repeat',
            name='repeat_on',
            field=models.DateField(),
        ),
    ]
