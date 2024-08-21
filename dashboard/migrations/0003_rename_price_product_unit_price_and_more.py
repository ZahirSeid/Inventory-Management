# Generated by Django 5.0.7 on 2024-08-21 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_alter_order_order_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='unit_price',
        ),
        migrations.AddField(
            model_name='product',
            name='serial_number',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('received', 'Received'), ('returned', 'Returned'), ('denied', 'Denied')], default='pending', max_length=10),
        ),
    ]