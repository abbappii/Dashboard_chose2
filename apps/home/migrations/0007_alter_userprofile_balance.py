# Generated by Django 3.2.11 on 2022-02-19 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20220219_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=500.0, max_digits=6),
        ),
    ]