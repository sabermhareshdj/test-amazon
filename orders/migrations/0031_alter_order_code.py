# Generated by Django 4.2.4 on 2023-10-03 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0030_alter_order_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='5YALF590', max_length=10),
        ),
    ]