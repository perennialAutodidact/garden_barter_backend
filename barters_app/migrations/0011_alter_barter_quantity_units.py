# Generated by Django 4.0.4 on 2022-05-29 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barters_app', '0010_alter_barter_date_expires'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barter',
            name='quantity_units',
            field=models.CharField(choices=[('PL', 'plant'), ('BC', 'bunch'), ('CT', 'count'), ('PK', 'package'), ('OZ', 'ounce'), ('LB', 'pound'), ('CY', 'cubic yard'), ('GL', 'gallon'), ('PT', 'pint')], default='CT', max_length=2, verbose_name='units'),
        ),
    ]
