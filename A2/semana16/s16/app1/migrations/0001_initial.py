# Generated by Django 5.1.3 on 2024-11-06 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='gmusic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ngmusic', models.CharField(max_length=100)),
                ('fgmusic', models.IntegerField()),
                ('artista', models.CharField(max_length=100)),
            ],
        ),
    ]
