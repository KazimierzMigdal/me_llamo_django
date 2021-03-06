# Generated by Django 3.0.5 on 2020-04-10 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('memo_card', '0002_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemoCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('esp_title', models.CharField(max_length=200)),
                ('esp_eg', models.TextField(blank=True, null=True)),
                ('pl_title', models.CharField(max_length=200)),
                ('pl_eg', models.TextField(blank=True, null=True)),
                ('grup', models.CharField(blank=True, choices=[('Shop', 'Shop'), ('Activity', 'Activity'), ('Time', 'Time'), ('Hospital', 'Hospital'), ('Apparition', 'Apparition'), ('Family', 'Family'), ('Meeting', 'Meeting'), ('Phone', 'Phone'), ('Opinion', 'Opinion'), ('Profesion', 'Profesion'), ('Relation', 'Relation'), ('Emotions', 'Emotions')], max_length=20, null=True)),
                ('esp_bold', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
