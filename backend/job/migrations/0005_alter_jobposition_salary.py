# Generated by Django 5.1.2 on 2024-10-12 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_jobposition_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobposition',
            name='salary',
            field=models.IntegerField(default=0),
        ),
    ]
