# Generated by Django 5.0.6 on 2024-05-14 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gridCRUD', '0004_alter_film_runningtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='genre',
            field=models.CharField(blank=True, help_text='영화 장르', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='posterImg',
            field=models.URLField(blank=True, help_text='포스터 이미지 URL', max_length=700, null=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='release',
            field=models.DateField(blank=True, help_text='개봉일', null=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='runningTime',
            field=models.IntegerField(blank=True, help_text='영화 러닝 타임, minute', null=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='subtitle',
            field=models.CharField(blank=True, help_text='영화 부제목', max_length=500, null=True),
        ),
    ]