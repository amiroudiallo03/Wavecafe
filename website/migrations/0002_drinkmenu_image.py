# Generated by Django 3.2.4 on 2021-06-03 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='drinkmenu',
            name='image',
            field=models.FileField(default=1, upload_to='drink_menu_image'),
            preserve_default=False,
        ),
    ]
