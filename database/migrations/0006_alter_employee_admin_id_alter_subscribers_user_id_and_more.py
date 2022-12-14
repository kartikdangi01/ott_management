# Generated by Django 4.1.3 on 2022-11-19 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0005_subscribers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='admin_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.administrator'),
        ),
        migrations.AlterField(
            model_name='subscribers',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.user'),
        ),
        migrations.AlterField(
            model_name='user',
            name='employee_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.employee'),
        ),
    ]
