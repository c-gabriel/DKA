# Generated by Django 2.0 on 2018-01-28 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dicionario', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='word',
            name='word_cr_id',
        ),
        migrations.RemoveField(
            model_name='word',
            name='word_en_id',
        ),
        migrations.RemoveField(
            model_name='word',
            name='word_pt_id',
        ),
    ]
