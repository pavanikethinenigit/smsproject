# Generated by Django 5.0.7 on 2024-10-18 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0002_studentlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('experience', models.CharField(max_length=20)),
                ('usability', models.CharField(max_length=20)),
                ('features', models.CharField(blank=True, max_length=200)),
                ('comments', models.TextField(blank=True)),
                ('recommend', models.CharField(max_length=3)),
            ],
        ),
    ]