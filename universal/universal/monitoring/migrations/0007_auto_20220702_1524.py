# Generated by Django 3.1.5 on 2022-07-02 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0006_auto_20220702_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='installed_devices',
            name='systems',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoring.system', verbose_name='Система'),
        ),
    ]
