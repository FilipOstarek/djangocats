# Generated by Django 3.2 on 2021-05-12 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0015_auto_20210512_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='description_of_the_cat',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='species',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]