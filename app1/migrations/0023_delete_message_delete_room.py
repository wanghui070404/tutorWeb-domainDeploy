# Generated by Django 5.0.3 on 2024-05-07 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0022_paymentrecord'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.DeleteModel(
            name='Room',
        ),
    ]
