# Generated by Django 3.0a1 on 2019-09-28 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0004_auto_20190928_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_logo',
            field=models.CharField(default='', max_length=200),
        ),
    ]
