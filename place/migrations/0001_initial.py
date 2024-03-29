# Generated by Django 3.0.2 on 2021-12-16 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='place_logo.png', upload_to='places_pp')),
                ('name', models.CharField(default='places', max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('highlight', models.TextField(blank=True)),
            ],
        ),
    ]
