# Generated by Django 3.0a1 on 2019-09-27 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='file_type',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='song',
            name='son_title',
            field=models.CharField(max_length=100),
        ),
    ]