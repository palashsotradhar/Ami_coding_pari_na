# Generated by Django 3.2.13 on 2022-11-10 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('khoj_the_search', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='khojm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('input_values', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]