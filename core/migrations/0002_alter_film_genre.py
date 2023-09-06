# Generated by Django 4.2.4 on 2023-09-06 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='genre',
            field=models.CharField(choices=[('horror', 'HORROR'), ('drama', 'DRAMA'), ('fantasy', 'FANTASY'), ('action', 'ACTION'), ('science fiction', 'SCIENCE FICTION'), ('drama', 'DRAMA'), ('thriller', 'THRILLER'), ('western', 'WESTERN'), ('comedy', 'COMEDY'), ('educational', 'EDUCATIONAL')], max_length=20),
        ),
    ]
