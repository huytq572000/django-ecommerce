# Generated by Django 4.0.4 on 2022-06-03 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_rename_completer_order_complete'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='spate',
            new_name='state',
        ),
    ]
