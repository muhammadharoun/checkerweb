# Generated by Django 3.1.7 on 2021-03-11 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Polo_Id',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=50)),
                ('polo_id', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PoloBrand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_sku', models.CharField(max_length=50)),
                ('has_variations', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=50)),
                ('sku1', models.CharField(blank=True, max_length=50, null=True)),
                ('variation1', models.CharField(blank=True, max_length=15, null=True)),
                ('sku2', models.CharField(blank=True, max_length=50, null=True)),
                ('variation2', models.CharField(blank=True, max_length=15, null=True)),
                ('sku3', models.CharField(blank=True, max_length=50, null=True)),
                ('variation3', models.CharField(blank=True, max_length=15, null=True)),
                ('sku4', models.CharField(blank=True, max_length=50, null=True)),
                ('variation4', models.CharField(blank=True, max_length=15, null=True)),
                ('sku5', models.CharField(blank=True, max_length=50, null=True)),
                ('variation5', models.CharField(blank=True, max_length=15, null=True)),
                ('sku6', models.CharField(blank=True, max_length=50, null=True)),
                ('variation6', models.CharField(blank=True, max_length=15, null=True)),
                ('sku7', models.CharField(blank=True, max_length=50, null=True)),
                ('variation7', models.CharField(blank=True, max_length=15, null=True)),
                ('sku8', models.CharField(blank=True, max_length=50, null=True)),
                ('variation8', models.CharField(blank=True, max_length=15, null=True)),
                ('sku9', models.CharField(blank=True, max_length=50, null=True)),
                ('variation9', models.CharField(blank=True, max_length=15, null=True)),
                ('sku10', models.CharField(blank=True, max_length=50, null=True)),
                ('variation10', models.CharField(blank=True, max_length=15, null=True)),
                ('sku11', models.CharField(blank=True, max_length=50, null=True)),
                ('variation11', models.CharField(blank=True, max_length=15, null=True)),
                ('sku12', models.CharField(blank=True, max_length=50, null=True)),
                ('variation12', models.CharField(blank=True, max_length=15, null=True)),
                ('sku13', models.CharField(blank=True, max_length=50, null=True)),
                ('variation13', models.CharField(blank=True, max_length=15, null=True)),
                ('sku14', models.CharField(blank=True, max_length=50, null=True)),
                ('variation14', models.CharField(blank=True, max_length=15, null=True)),
                ('sku15', models.CharField(blank=True, max_length=50, null=True)),
                ('variation15', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reverse_check',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=50)),
            ],
        ),
    ]