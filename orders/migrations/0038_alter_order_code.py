# Generated by Django 4.2.4 on 2023-11-28 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0037_alter_order_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='RBBCNK4U', max_length=10),
        ),
    ]
