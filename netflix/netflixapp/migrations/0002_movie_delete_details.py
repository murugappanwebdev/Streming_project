# Generated by Django 5.0.6 on 2024-07-05 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netflixapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('genre', models.IntegerField(choices=[(1, 'Action and Adventure'), (2, 'Comedy'), (3, 'Drama'), (4, 'Horror'), (5, 'Romance'), (6, 'Sci-Fi')])),
                ('description', models.TextField(max_length=500)),
                ('cover_image', models.ImageField(upload_to='media/')),
            ],
        ),
        migrations.DeleteModel(
            name='Details',
        ),
    ]