# Generated by Django 3.0.3 on 2020-03-03 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20200303_1945'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productinorder',
            options={'verbose_name': 'Товар в заказе ', 'verbose_name_plural': 'Товары в заказе'},
        ),
    ]