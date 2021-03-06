# Generated by Django 4.0.4 on 2022-06-23 20:16

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=25)),
                ('birth_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imdb_id', models.CharField(max_length=255)),
                ('title_type', models.CharField(choices=[('Short', 'Short-movie'), ('Movie', 'Movie')], max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('is_adult', models.BooleanField(null=True)),
                ('year', models.DateField(null=True)),
                ('genres', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imdb_id', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('birth_year', models.DateField(null=True)),
                ('death_year', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PersonMovie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(null=True)),
                ('category', models.CharField(max_length=200)),
                ('job', models.CharField(max_length=200)),
                ('characters', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), default=list, size=None)),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.movie')),
                ('person_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.person')),
            ],
        ),
    ]
