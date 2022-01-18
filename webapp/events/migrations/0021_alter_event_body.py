# Generated by Django 3.2 on 2022-01-18 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0020_alter_event_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='body',
            field=models.CharField(blank=True, help_text='Enter valid GitHub markdown -\n    <a href="https://docs.github.com/en/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax" target="_blank">see markdown guide</a>.\n    We\'re using <b>"code-friendly" mode</b>, so __ and _ will be rendered\n    literally! Use * and ** for italics/bold instead.\n    \n    <br>\n    Upload event images at the bottom of the page, and tag them\n    in markdown like so:\n    <pre>\n     <span style="color: #79AEC8"># the URI will replace img&lt;N&gt; after save </span>\n     ![alt text](img1)\n\n     <span style="color: #79AEC8"># Use an image tag to define size. Defaults to 100% max-width.</span>\n     &lt;img src="img2" width=200&gt; </pre>\n     ', max_length=50000, null=True),
        ),
    ]
