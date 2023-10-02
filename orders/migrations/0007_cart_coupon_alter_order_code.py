# Generated by Django 4.2.4 on 2023-10-02 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_alter_order_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='Coupon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cart_coupon', to='orders.coupon'),
        ),
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='39BVOYRM', max_length=10),
        ),
    ]
