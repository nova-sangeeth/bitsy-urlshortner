# Generated by Django 3.0.7 on 2020-07-13 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200702_2007'),
    ]

    operations = [
        migrations.AddField(
            model_name='short_urls',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
