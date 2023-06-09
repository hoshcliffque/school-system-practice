# Generated by Django 4.1.7 on 2023-03-15 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_person_remove_student_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='accounts.person')),
            ],
            bases=('accounts.person',),
        ),
        migrations.RemoveField(
            model_name='person',
            name='parent_name',
        ),
    ]
