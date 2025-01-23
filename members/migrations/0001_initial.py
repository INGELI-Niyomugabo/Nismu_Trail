# Generated by Django 5.1.2 on 2024-10-10 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('level', models.IntegerField()),
                ('school', models.FloatField(max_length=255)),
                ('images_url', models.CharField(max_length=2083)),
            ],
        ),
        migrations.CreateModel(
            name='results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField()),
                ('comment', models.CharField(max_length=2083)),
                ('reward', models.FloatField(max_length=255)),
            ],
        ),
    ]
