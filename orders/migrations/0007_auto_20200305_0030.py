# Generated by Django 3.0.3 on 2020-03-04 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20200303_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinorder',
            name='nmb',
            field=models.IntegerField(default=1),
        ),
    ]
