# Generated by Django 2.1.7 on 2019-03-19 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salah', '0006_auto_20190317_1140'),
    ]

    operations = [
        migrations.CreateModel(
            name='Umages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.ImageField(blank=True, default='default.png', upload_to='')),
            ],
        ),
    ]
