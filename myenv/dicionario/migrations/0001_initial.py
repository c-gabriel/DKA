# Generated by Django 2.0.1 on 2018-01-20 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word_en_id', models.BigIntegerField()),
                ('word_cr_id', models.BigIntegerField()),
                ('word_pt_id', models.BigIntegerField()),
                ('word_en', models.TextField()),
                ('word_cr', models.TextField()),
                ('word_pt', models.TextField()),
                ('descr', models.TextField()),
            ],
        ),
    ]
