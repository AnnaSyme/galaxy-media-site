# Generated by Django 3.2 on 2022-02-25 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_notice_display_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='display_title',
            field=models.BooleanField(default=True, help_text='Uncheck to hide the title when displaying the notice.'),
        ),
    ]
