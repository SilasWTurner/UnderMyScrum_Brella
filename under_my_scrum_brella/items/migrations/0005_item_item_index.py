# Generated by Django 5.1.dev20240130101038 on 2024-02-27 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_alter_useritem_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_index',
            field=models.IntegerField(default=0),
        ),
    ]
