# Generated by Django 3.2.7 on 2022-05-23 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tibikon', '0002_saints_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saints',
            name='name',
            field=models.CharField(default='none', max_length=255, verbose_name='الاسم'),
        ),
    ]