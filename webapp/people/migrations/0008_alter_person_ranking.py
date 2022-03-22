# Generated by Django 4.0.3 on 2022-03-22 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0007_remove_person_phone_person_ranking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='ranking',
            field=models.IntegerField(blank=True, default=99, help_text='Profiles are ordered first by ascending rank, and then by date created (oldest first). To order by date created, leave the default of 99.'),
        ),
    ]
