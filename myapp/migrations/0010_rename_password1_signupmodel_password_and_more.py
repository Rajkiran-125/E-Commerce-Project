# Generated by Django 4.1.3 on 2022-12-07 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_delete_loginmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signupmodel',
            old_name='password1',
            new_name='password',
        ),
        migrations.RemoveField(
            model_name='signupmodel',
            name='password2',
        ),
    ]