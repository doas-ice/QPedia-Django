# Generated by Django 4.0.3 on 2022-03-20 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedia_app', '0002_alter_tournies_tier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournies',
            name='tier',
            field=models.CharField(max_length=1),
        ),
    ]
