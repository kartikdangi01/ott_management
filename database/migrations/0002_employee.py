# Generated by Django 4.1.3 on 2022-11-17 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.IntegerField()),
                ('employee_name', models.CharField(max_length=255)),
                ('admin_id', models.IntegerField()),
            ],
            options={
                'db_table': 'Employee',
            },
        ),
    ]
