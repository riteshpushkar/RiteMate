# Generated by Django 4.0 on 2024-04-22 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0012_listing_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='email',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
    ]
