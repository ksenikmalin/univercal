# Generated by Django 3.1.5 on 2022-07-02 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0008_auto_20220702_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='system',
            name='photo',
            field=models.ImageField(default=123, upload_to='', verbose_name='Иконка'),
            preserve_default=False,
        ),
    ]
