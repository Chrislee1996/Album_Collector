# Generated by Django 3.0 on 2022-04-18 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=100)),
                ('albumName', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
                ('yearOfRelease', models.IntegerField()),
            ],
        ),
    ]
