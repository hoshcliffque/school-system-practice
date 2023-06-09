# Generated by Django 4.1.7 on 2023-03-15 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('dob', models.DateField()),
                ('sex', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('date_of_join', models.DateField(auto_now_add=True)),
                ('parent_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='address',
        ),
        migrations.RemoveField(
            model_name='student',
            name='date_of_join',
        ),
        migrations.RemoveField(
            model_name='student',
            name='dob',
        ),
        migrations.RemoveField(
            model_name='student',
            name='email',
        ),
        migrations.RemoveField(
            model_name='student',
            name='id',
        ),
        migrations.RemoveField(
            model_name='student',
            name='name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='parent_name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='password',
        ),
        migrations.RemoveField(
            model_name='student',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='student',
            name='sex',
        ),
        migrations.AddField(
            model_name='student',
            name='person_ptr',
            field=models.OneToOneField(auto_created=True, default='', on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='accounts.person'),
            preserve_default=False,
        ),
    ]
