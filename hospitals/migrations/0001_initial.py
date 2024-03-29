# Generated by Django 3.0.2 on 2021-12-16 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='hospital_pp')),
                ('name', models.CharField(default='hospital', max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('facility', models.TextField(blank=True)),
                ('contact', models.TextField(blank=True)),
            ],
        ),
    ]
