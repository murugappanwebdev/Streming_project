# Generated by Django 5.0.6 on 2024-06-06 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('mobile', models.CharField(max_length=11)),
                ('email', models.CharField(max_length=35)),
                ('password', models.CharField(max_length=35)),
            ],
        ),
    ]
