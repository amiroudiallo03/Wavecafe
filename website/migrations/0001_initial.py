# Generated by Django 3.2.4 on 2021-06-02 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('titre', models.CharField(max_length=100)),
                ('sous_titre', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.FileField(upload_to='image')),
            ],
            options={
                'verbose_name': 'About',
                'verbose_name_plural': 'Abouts',
            },
        ),
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('nom', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Categorie',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('nom', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
        ),
        migrations.CreateModel(
            name='DrinkMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('nom', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('prix', models.FloatField()),
            ],
            options={
                'verbose_name': 'DrinkMenu',
                'verbose_name_plural': 'DrinkMenu',
            },
        ),
        migrations.CreateModel(
            name='SpecialItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('image', models.FileField(upload_to='image_items')),
                ('titre', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'SpecialItems',
                'verbose_name_plural': 'SpecialItems',
            },
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('logo', models.FileField(upload_to='')),
                ('nom_site', models.CharField(max_length=100)),
                ('copyright', models.CharField(max_length=100)),
                ('titre_contact', models.CharField(max_length=100)),
                ('description_contact', models.TextField()),
                ('titre_about', models.CharField(max_length=100)),
                ('image_about', models.FileField(upload_to='image_about')),
                ('description_about', models.TextField()),
            ],
            options={
                'verbose_name': 'Website',
                'verbose_name_plural': 'Websites',
            },
        ),
    ]
