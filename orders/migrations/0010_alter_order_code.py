# Generated by Django 4.2.4 on 2023-10-02 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_cartdetail_total_after_coupon_alter_order_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='N14LO8L6', max_length=10),
        ),
    ]
