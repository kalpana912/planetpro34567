# Generated by Django 4.1.5 on 2023-01-31 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.URLField(default='https://www.facebook.com/kalpana.choudhary.777363', max_length=500)),
                ('instagram', models.URLField(default='https://www.instagram.com/kalpana91295', max_length=500)),
                ('twitter', models.URLField(default='https://www.twitter.com/', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='InformationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('cardimage', models.ImageField(null=True, upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='PlanetModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background_picture', models.ImageField(null=True, upload_to='media')),
                ('small_heading', models.CharField(default='Are you a tech trainer, influencer or expert?', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('mobileNumber', models.CharField(max_length=11)),
                ('mail', models.EmailField(default='abc@gmail.com', max_length=254)),
            ],
            options={
                'db_table': 'User',
            },
        ),
    ]
