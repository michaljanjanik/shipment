# Generated by Django 3.2.13 on 2022-06-27 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deliveries', '0002_auto_20220627_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='delivery_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='date delivered'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='send_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='date sended'),
        ),
    ]