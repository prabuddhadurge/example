# Generated by Django 3.2.11 on 2022-01-30 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20220130_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='id',
            field=models.CharField(max_length=40, primary_key=True, serialize=False),
        ),
    ]