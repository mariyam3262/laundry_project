# Generated by Django 4.0.3 on 2022-05-18 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0002_alter_expense_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='amount',
            field=models.CharField(default=0, max_length=30),
        ),
    ]
