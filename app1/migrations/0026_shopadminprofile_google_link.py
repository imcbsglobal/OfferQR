# Generated by Django 5.0.6 on 2024-10-11 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0025_shopadminprofile_facebook_link_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopadminprofile',
            name='google_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
