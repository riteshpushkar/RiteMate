# Generated by Django 4.0 on 2024-03-14 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0004_rename_image1_listing_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='image_self',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='occupancy',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='occupation',
        ),
        migrations.AlterField(
            model_name='listing',
            name='description',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='listing',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('any', 'Any')], max_length=6),
        ),
        migrations.AlterField(
            model_name='listing',
            name='image',
            field=models.ImageField(upload_to='RiteMate_project\\media\\properties_images'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='location',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='listing',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='listing',
            name='rent',
            field=models.IntegerField(),
        ),
    ]