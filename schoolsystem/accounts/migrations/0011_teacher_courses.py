# Generated by Django 4.1.7 on 2023-03-15 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_remove_course_id_course_course_code_result_class'),
        ('accounts', '0010_student_courses'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='courses',
            field=models.ManyToManyField(related_name='teachers', to='courses.course'),
        ),
    ]