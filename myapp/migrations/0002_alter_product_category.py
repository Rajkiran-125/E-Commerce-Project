# Generated by Django 4.1.3 on 2022-12-06 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('M', 'Manswear'), ('W', 'Womanswear'), ('A', 'Accessories'), ('N', 'NewArrivals'), ('F', 'Featured')], max_length=5),
        ),
    ]
