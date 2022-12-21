# Generated by Django 4.1.2 on 2022-12-21 21:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=20)),
                ('semester', models.CharField(choices=[('Spring', 'Spring'), ('Fall', 'Fall'), ('Summer', 'Summer'), ('Winter', 'Winter')], default='Fall', max_length=10)),
                ('days', models.CharField(max_length=60)),
                ('time_start', models.TimeField(blank=True, null=True)),
                ('time_end', models.TimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('time', models.TimeField()),
                ('date', models.DateField()),
                ('message', models.CharField(max_length=500)),
                ('role', models.CharField(choices=[('Supervisor', 'Supervisor'), ('Instructor', 'Instructor'), ('TA', 'Ta')], default='TA', max_length=10)),
                ('email', models.EmailField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=25)),
                ('role', models.CharField(choices=[('Supervisor', 'Supervisor'), ('Instructor', 'Instructor'), ('TA', 'Ta')], default='TA', max_length=10)),
                ('email', models.CharField(max_length=40)),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_num', models.CharField(max_length=3)),
                ('days', models.CharField(max_length=601)),
                ('time_start', models.TimeField(blank=True, null=True)),
                ('time_end', models.TimeField(blank=True, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchedulingAPP.course')),
                ('ta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchedulingAPP.user')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='instructor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchedulingAPP.user'),
        ),
    ]
