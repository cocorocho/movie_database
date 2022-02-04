# Generated by Django 3.2.7 on 2022-02-04 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Directors',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name_plural': 'Genres',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Languages',
            },
        ),
        migrations.CreateModel(
            name='Poster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.FileField(max_length=500, null=True, upload_to='p')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('year', models.IntegerField(null=True)),
                ('description', models.TextField(max_length=900, null=True)),
                ('score_imdb', models.IntegerField(null=True)),
                ('score_rotten_tomatoes_critic', models.IntegerField(null=True)),
                ('score_rotten_tomatoes_audience', models.IntegerField(null=True)),
                ('score_metacritic_viewer', models.FloatField(null=True)),
                ('score_metacritic_critic', models.FloatField(null=True)),
                ('imdb_id', models.CharField(max_length=100, null=True)),
                ('tmdb_id', models.IntegerField(null=True)),
                ('adult', models.BooleanField(null=True)),
                ('vote_count_imdb', models.CharField(max_length=100, null=True)),
                ('vote_count_metacritic_viewer', models.CharField(max_length=100, null=True)),
                ('vote_count_metacritic_critic', models.CharField(max_length=100, null=True)),
                ('genres', models.ManyToManyField(to='movies.Genre')),
                ('language', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movies.language')),
                ('poster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.poster')),
            ],
            options={
                'verbose_name_plural': 'Movies',
            },
        ),
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('movies', models.ManyToManyField(to='movies.Movie')),
            ],
            options={
                'verbose_name_plural': 'Actors',
            },
        ),
    ]
