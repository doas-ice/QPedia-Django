# Generated by Django 4.0.3 on 2022-03-20 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Matches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tournament', models.IntegerField()),
                ('team1', models.IntegerField()),
                ('team2', models.IntegerField()),
                ('score1', models.IntegerField()),
                ('score2', models.IntegerField()),
                ('time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('region', models.CharField(max_length=50)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='teams/uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='Tournies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tier', models.CharField(max_length=1)),
                ('name', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=50)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='tournies/uploads/')),
                ('date_start', models.DateTimeField()),
                ('date_end', models.DateTimeField()),
                ('is_finished', models.BooleanField(blank=True, null=True)),
                ('winner', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
