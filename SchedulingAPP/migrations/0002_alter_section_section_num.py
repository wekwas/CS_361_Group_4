# Generated by Django 4.1.3 on 2022-12-06 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SchedulingAPP', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='section_num',
            field=models.CharField(max_length=3),
        ),
    ]