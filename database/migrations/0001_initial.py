# Generated by Django 4.1.3 on 2022-11-17 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_id', models.IntegerField()),
                ('admin_name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'Administrator',
            },
        ),
    ]
