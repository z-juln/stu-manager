# Generated by Django 3.1.3 on 2020-12-01 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stuManager', '0002_manager_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='password',
            field=models.CharField(max_length=10),
        ),
    ]
