# Generated by Django 3.1.4 on 2022-01-26 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='coverpic',
            field=models.ImageField(default='', upload_to='post'),
            preserve_default=False,
        ),
    ]
