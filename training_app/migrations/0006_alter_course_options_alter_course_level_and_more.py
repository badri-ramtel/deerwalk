# Generated by Django 4.2 on 2023-05-03 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training_app', '0005_alter_course_description_alter_course_duration_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name_plural': 'Courses'},
        ),
        migrations.AlterField(
            model_name='course',
            name='level',
            field=models.CharField(choices=[('B', 'Beginner'), ('I', 'Intermediate'), ('A', 'Advance')], default='B', max_length=1),
        ),
        migrations.AlterModelTable(
            name='course',
            table='Course',
        ),
    ]
