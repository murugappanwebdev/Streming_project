# Generated by Django 5.0.6 on 2024-07-08 05:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('netflixapp', '0005_movies_delete_movie'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Movies',
        ),
    ]
