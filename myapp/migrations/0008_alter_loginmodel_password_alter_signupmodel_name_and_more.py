# Generated by Django 4.1.3 on 2022-12-07 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_loginmodel_signupmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginmodel',
            name='password',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='signupmodel',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='signupmodel',
            name='password1',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='signupmodel',
            name='password2',
            field=models.CharField(max_length=50),
        ),
    ]
