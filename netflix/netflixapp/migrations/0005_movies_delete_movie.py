# Generated by Django 5.0.6 on 2024-07-06 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netflixapp', '0004_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('cast', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('description', models.TextField(max_length=500)),
                ('cover_image', models.ImageField(upload_to='media/')),
            ],
        ),
        migrations.DeleteModel(
            name='Movie',
        ),
    ]