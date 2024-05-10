# Generated by Django 5.0.6 on 2024-05-10 07:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gridCRUD', '0002_remove_film_director_id_film_director'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='director',
            field=models.ForeignKey(help_text='제작자', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='films', to='gridCRUD.director'),
        ),
    ]
