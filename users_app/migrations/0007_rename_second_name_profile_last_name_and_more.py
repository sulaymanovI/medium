# Generated by Django 5.0.1 on 2024-05-29 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0006_alter_user_birth_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='second_name',
            new_name='last_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
    ]
