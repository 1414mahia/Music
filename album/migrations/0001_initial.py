# Generated by Django 5.1.1 on 2024-10-09 14:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('musician', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=20)),
                ('release_date', models.DateField()),
                ('instrument', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], max_length=10)),
                ('musician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='musician.musicmodel')),
            ],
        ),
    ]
