# Generated by Django 3.0.7 on 2020-07-13 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200713_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='short_urls',
            name='slug',
            field=models.CharField(max_length=16, null=True),
        ),
    ]
