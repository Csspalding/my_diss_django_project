# Generated by Django 2.1.5 on 2019-09-02 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cupcake_site', '0005_auto_20190829_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(blank=True, upload_to='profile_images/'),
        ),
    ]
