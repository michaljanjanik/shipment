# Generated by Django 3.2.13 on 2022-06-27 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("deliveries", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="delivery",
            name="delivery_date",
            field=models.DateTimeField(null=True, verbose_name="date delivered"),
        ),
        migrations.AlterField(
            model_name="delivery",
            name="send_date",
            field=models.DateTimeField(null=True, verbose_name="date sended"),
        ),
    ]
