# Generated by Django 3.1.5 on 2021-01-29 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opportunity', '0002_auto_20210129_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='opportunity',
            name='name',
            field=models.CharField(default='name', max_length=50),
        ),
    ]
