# Generated by Django 3.0a1 on 2019-10-03 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0006_auto_20191002_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='son_logo',
            field=models.CharField(default='', max_length=100),
        ),
    ]