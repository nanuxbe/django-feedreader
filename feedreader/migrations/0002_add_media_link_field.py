# Generated by Django 3.0.8 on 2020-07-18 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedreader', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='media_link',
            field=models.URLField(blank=True, max_length=2000, null=True),
        ),
    ]
