# Generated by Django 3.2.8 on 2021-10-31 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20211031_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request_sent',
            name='status',
            field=models.CharField(default='', max_length=255, null=True),
        ),
    ]
