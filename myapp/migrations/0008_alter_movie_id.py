# Generated by Django 3.2.11 on 2022-01-30 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_movie_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='id',
            field=models.TextField(max_length=40, primary_key=True, serialize=False, unique=True),
        ),
    ]
