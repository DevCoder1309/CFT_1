# Generated by Django 4.2.2 on 2023-07-27 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_alter_comment_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='message',
            new_name='comment',
        ),
    ]
