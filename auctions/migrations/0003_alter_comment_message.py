# Generated by Django 4.2.2 on 2023-07-24 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_remove_active_listening_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='message',
            field=models.CharField(max_length=255),
        ),
    ]
