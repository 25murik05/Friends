# Generated by Django 4.0.5 on 2022-06-23 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_user_birth_alter_user_email_alter_user_login_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
