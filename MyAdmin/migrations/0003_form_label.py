# Generated by Django 3.0 on 2020-03-15 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyAdmin', '0002_auto_20200315_1813'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='Label',
            field=models.CharField(default='', max_length=100),
        ),
    ]
