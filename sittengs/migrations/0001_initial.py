# Generated by Django 3.1.7 on 2021-03-13 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sittenge_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_token', models.CharField(max_length=300)),
                ('STORE_ID', models.CharField(max_length=300)),
            ],
        ),
    ]
