# Generated by Django 5.0.1 on 2024-02-12 19:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("roomschedulerapi", "0004_course_instructor"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="course_level",
            field=models.CharField(max_length=5),
        ),
    ]