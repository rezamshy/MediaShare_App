# Generated by Django 4.2.2 on 2023-06-19 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='rate',
            field=models.DecimalField(decimal_places=1, default=9, max_digits=2),
            preserve_default=False,
        ),
    ]