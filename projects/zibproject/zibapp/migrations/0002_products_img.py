# Generated by Django 4.2.1 on 2023-05-26 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zibapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='img',
            field=models.ImageField(default=0, upload_to='pics'),
            preserve_default=False,
        ),
    ]
