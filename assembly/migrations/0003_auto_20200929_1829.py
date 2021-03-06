# Generated by Django 3.1.1 on 2020-09-29 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assembly', '0002_auto_20200901_0146'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemprofile',
            name='sub_tasks',
            field=models.TextField(default='List of tasks in stations in order.'),
        ),
        migrations.AlterField(
            model_name='itemprofile',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='assembly.item'),
        ),
        migrations.AlterField(
            model_name='itemprofile',
            name='stations',
            field=models.TextField(default='List of stations in order.'),
        ),
    ]
