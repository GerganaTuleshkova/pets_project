# Generated by Django 4.0.2 on 2022-02-24 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet_app', '0002_alter_petphoto_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petphoto',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
