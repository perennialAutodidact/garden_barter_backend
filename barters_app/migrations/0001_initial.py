# Generated by Django 4.0.4 on 2022-05-02 19:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Barter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, max_length=255, verbose_name='title')),
                ('description', models.CharField(max_length=1000, verbose_name='description')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='date updated')),
                ('date_expires', models.DateTimeField(verbose_name='expires on')),
                ('postal_code', models.CharField(max_length=12, verbose_name='postal code')),
                ('will_trade_for', models.CharField(max_length=255, verbose_name='will trade for')),
                ('is_free', models.BooleanField(default=False, verbose_name='free')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='barters', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MaterialBarter',
            fields=[
                ('barter_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='barters_app.barter')),
            ],
            bases=('barters_app.barter',),
        ),
        migrations.CreateModel(
            name='PlantBarter',
            fields=[
                ('barter_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='barters_app.barter')),
                ('genus', models.CharField(blank=True, max_length=255, null=True, verbose_name='genus')),
                ('species', models.CharField(blank=True, max_length=255, null=True, verbose_name='species')),
                ('common_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='common_name')),
                ('age', models.CharField(blank=True, max_length=255, null=True)),
            ],
            bases=('barters_app.barter',),
        ),
        migrations.CreateModel(
            name='SeedBarter',
            fields=[
                ('barter_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='barters_app.barter')),
                ('genus', models.CharField(blank=True, max_length=255, null=True, verbose_name='genus')),
                ('species', models.CharField(blank=True, max_length=255, null=True, verbose_name='species')),
                ('common_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='common_name')),
                ('date_packaged', models.DateField(null=True, verbose_name='date_packaged')),
            ],
            bases=('barters_app.barter',),
        ),
        migrations.CreateModel(
            name='ToolBarter',
            fields=[
                ('barter_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='barters_app.barter')),
            ],
            bases=('barters_app.barter',),
        ),
        migrations.CreateModel(
            name='ProduceBarter',
            fields=[
                ('plantbarter_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='barters_app.plantbarter')),
                ('date_harvested', models.DateField(null=True)),
            ],
            bases=('barters_app.plantbarter',),
        ),
    ]