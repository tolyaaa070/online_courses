# Generated by Django 5.2.1 on 2025-05-19 13:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses_app', '0003_alter_assignment_course_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='course_image',
            field=models.ImageField(default=1, upload_to='course_images/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='courses_app.courses'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='review',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='courses_app.courses'),
        ),
    ]
