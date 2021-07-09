# Generated by Django 3.1 on 2021-06-28 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pieces', models.IntegerField(default=0)),
                ('feet', models.CharField(max_length=200, null=True)),
                ('mm', models.CharField(max_length=200, null=True)),
                ('types', models.CharField(max_length=200, null=True)),
                ('company', models.CharField(max_length=200, null=True)),
                ('color', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]