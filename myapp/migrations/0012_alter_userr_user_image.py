# Generated by Django 5.0.3 on 2024-05-13 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_alter_userr_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userr',
            name='user_image',
            field=models.ImageField(blank=True, null=True, upload_to='user_image/'),
        ),
    ]
