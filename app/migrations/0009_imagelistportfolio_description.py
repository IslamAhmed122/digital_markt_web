# Generated by Django 3.2.9 on 2021-11-15 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_imagelistportfolio_alt'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagelistportfolio',
            name='description',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
