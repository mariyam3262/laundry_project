# Generated by Django 4.0.4 on 2022-05-13 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='register_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]