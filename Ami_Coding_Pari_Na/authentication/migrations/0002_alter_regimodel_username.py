# Generated by Django 3.2.13 on 2022-11-08 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regimodel',
            name='username',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]