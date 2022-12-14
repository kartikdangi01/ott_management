# Generated by Django 4.1.3 on 2022-11-17 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('user_name', models.CharField(max_length=255)),
                ('phone_number', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('watch_hours', models.IntegerField()),
                ('employee_id', models.IntegerField()),
            ],
            options={
                'db_table': 'Users',
            },
        ),
    ]
