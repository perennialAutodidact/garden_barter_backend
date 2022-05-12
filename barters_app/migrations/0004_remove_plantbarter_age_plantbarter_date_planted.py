# Generated by Django 4.0.4 on 2022-05-11 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barters_app', '0003_remove_seedbarter_date_packaged_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plantbarter',
            name='age',
        ),
        migrations.AddField(
            model_name='plantbarter',
            name='date_planted',
            field=models.DateField(blank=True, max_length=255, null=True),
        ),
    ]