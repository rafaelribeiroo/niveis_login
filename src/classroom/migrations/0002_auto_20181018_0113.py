# Generated by Django 2.0.1 on 2018-10-18 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='is_correct',
        ),
        migrations.AddField(
            model_name='answer',
            name='answer',
            field=models.BooleanField(default=False, verbose_name='Resposta'),
        ),
    ]