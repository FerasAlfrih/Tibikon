# Generated by Django 3.2.7 on 2021-10-12 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Saints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saint', models.CharField(max_length=255, verbose_name='saint')),
                ('day', models.IntegerField(verbose_name='day')),
                ('month', models.IntegerField(verbose_name='month')),
                ('feast', models.CharField(max_length=50, verbose_name='feast')),
            ],
        ),
    ]
