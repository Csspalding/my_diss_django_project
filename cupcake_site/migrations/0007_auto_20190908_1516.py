# Generated by Django 2.1.5 on 2019-09-08 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cupcake_site', '0006_auto_20190902_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(),
        ),
    ]
