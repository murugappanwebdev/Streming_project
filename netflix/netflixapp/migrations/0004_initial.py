# Generated by Django 5.0.6 on 2024-07-05 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('netflixapp', '0003_delete_movie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('year', models.IntegerField()),
                ('description', models.TextField(max_length=500)),
                ('cover_image', models.ImageField(upload_to='media/')),
            ],
        ),
    ]