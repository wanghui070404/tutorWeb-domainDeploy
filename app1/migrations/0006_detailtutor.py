# Generated by Django 5.0.3 on 2024-04-25 03:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_delete_detail_tutor'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DETAILTUTOR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('sex', models.CharField(max_length=3)),
                ('phone_number', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('school', models.CharField(max_length=50)),
                ('certificate', models.ImageField(upload_to='')),
                ('subject1', models.CharField(max_length=10)),
                ('subject2', models.CharField(max_length=10, null=True)),
                ('subject3', models.CharField(max_length=10, null=True)),
                ('Introduction', models.CharField(max_length=600)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]