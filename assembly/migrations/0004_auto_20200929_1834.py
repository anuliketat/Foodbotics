# Generated by Django 3.1.1 on 2020-09-29 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assembly', '0003_auto_20200929_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemprofile',
            name='stations',
            field=models.TextField(default='List of stations in order.', max_length=100),
        ),
        migrations.AlterField(
            model_name='itemprofile',
            name='sub_tasks',
            field=models.TextField(default='List of tasks in stations in order.', max_length=100),
        ),
    ]