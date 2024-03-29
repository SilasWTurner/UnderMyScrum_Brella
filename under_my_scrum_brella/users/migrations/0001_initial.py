# Generated by Django 5.0.2 on 2024-02-26 15:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('buddy_name', models.CharField(max_length=400)),
                ('buddy_type', models.CharField(max_length=400)),
                ('total_coins', models.IntegerField(default=0)),
                ('total_xp', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pending_first_second', models.BooleanField()),
                ('pending_second_first', models.BooleanField()),
                ('friends', models.BooleanField(default=False)),
                ('user1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='first_user', to=settings.AUTH_USER_MODEL)),
                ('user2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='second_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user1', 'user2')},
            },
        ),
    ]
