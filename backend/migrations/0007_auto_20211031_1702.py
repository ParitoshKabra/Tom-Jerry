# Generated by Django 3.2.8 on 2021-10-31 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_auto_20211031_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request_confirm',
            name='addressAttempt',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='request_confirm',
            name='passAttempt',
            field=models.IntegerField(default=0),
        ),
    ]
