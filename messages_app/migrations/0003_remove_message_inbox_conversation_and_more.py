# Generated by Django 4.0.4 on 2022-07-22 22:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('messages_app', '0002_message_body_alter_inbox_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='inbox',
        ),
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barter_id', models.PositiveIntegerField(verbose_name='barter id')),
                ('barter_type', models.CharField(max_length=10, verbose_name='barter type')),
                ('inbox', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conversations', to='messages_app.inbox')),
                ('participants', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='participants')),
                ('recipient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='conversations', to=settings.AUTH_USER_MODEL, verbose_name='recipient')),
                ('sender', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='coversations', to=settings.AUTH_USER_MODEL, verbose_name='sender')),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='conversation',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='messages_app.conversation', verbose_name='conversation'),
            preserve_default=False,
        ),
    ]