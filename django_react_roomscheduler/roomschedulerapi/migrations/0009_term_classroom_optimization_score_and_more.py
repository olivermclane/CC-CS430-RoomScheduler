# Generated by Django 5.0.1 on 2024-03-12 18:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roomschedulerapi', '0008_alter_building_image_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Term',
            fields=[
                ('term_id', models.AutoField(primary_key=True, serialize=False)),
                ('term_name', models.CharField(max_length=6)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='classroom',
            name='optimization_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='building',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='term',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='roomschedulerapi.term'),
        ),
    ]