# Generated by Django 4.2.4 on 2023-10-02 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_alter_order_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='NPPLPND4', max_length=10),
        ),
    ]