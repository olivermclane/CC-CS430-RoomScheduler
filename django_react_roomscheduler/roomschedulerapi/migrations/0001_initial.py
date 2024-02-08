# Generated by Django 5.0.1 on 2024-02-07 21:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('building_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('classroom_id', models.AutoField(primary_key=True, serialize=False)),
                ('class_room_number', models.IntegerField(default=0, max_length=3)),
                ('total_seats', models.IntegerField(default=0)),
                ('width_of_room', models.IntegerField(default=0)),
                ('length_of_room', models.IntegerField(default=0)),
                ('projectors', models.IntegerField(default=0)),
                ('microphone_system', models.BooleanField(default=0)),
                ('blueray_player', models.BooleanField(default=False)),
                ('laptop_hdmi', models.BooleanField(default=False)),
                ('zoom_camera', models.BooleanField(default=False)),
                ('document_camera', models.BooleanField(default=False)),
                ('storage', models.BooleanField(default=False)),
                ('movable_chairs', models.BooleanField(default=False)),
                ('printer', models.BooleanField(default=False)),
                ('piano', models.BooleanField(default=False)),
                ('stereo_system', models.BooleanField(default=False)),
                ('total_tv', models.IntegerField(default=0)),
                ('sinks', models.IntegerField(default=0)),
                ('notes', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.AutoField(primary_key=True, serialize=False)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('first_day', models.DateField()),
                ('last_day', models.DateField()),
                ('course_name', models.CharField(max_length=100)),
                ('term', models.CharField(blank=True, max_length=10)),
                ('credits', models.IntegerField(default=0)),
                ('course_cap', models.IntegerField(default=0)),
                ('waitlist_cap', models.IntegerField(default=0)),
                ('course_total', models.IntegerField(default=0)),
                ('waitlist_total', models.IntegerField(default=0)),
                ('enrollment_total', models.IntegerField(default=0)),
                ('course_level', models.CharField(max_length=3)),
                ('monday', models.BooleanField(default=False)),
                ('tuesday', models.BooleanField(default=False)),
                ('wednesday', models.BooleanField(default=False)),
                ('thursday', models.BooleanField(default=False)),
                ('friday', models.BooleanField(default=False)),
                ('saturday', models.BooleanField(default=False)),
                ('sunday', models.BooleanField(default=False)),
                ('classroom_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roomschedulerapi.classroom')),
            ],
        ),
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('floor_id', models.AutoField(primary_key=True, serialize=False)),
                ('floor_name', models.CharField(max_length=50)),
                ('building_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roomschedulerapi.building')),
            ],
        ),
        migrations.AddField(
            model_name='classroom',
            name='floor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roomschedulerapi.floor'),
        ),
    ]
