# Generated by Django 3.2.11 on 2022-01-30 19:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_movie_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='id',
            field=models.CharField(default=uuid.UUID('dcc9d668-81ff-11ec-979b-a86bad13344b'), max_length=40, primary_key=True, serialize=False),
        ),
    ]
