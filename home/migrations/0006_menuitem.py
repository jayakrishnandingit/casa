# Generated by Django 2.2 on 2020-07-13 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_homepage_portfolio'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('link', models.CharField(blank=True, help_text='Where do you want this to take you to?', max_length=1000, null=True)),
            ],
        ),
    ]