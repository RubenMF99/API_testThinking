# Generated by Django 3.2.4 on 2022-07-25 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyname', models.CharField(max_length=80)),
                ('direction', models.CharField(max_length=40)),
                ('NIT', models.PositiveIntegerField()),
                ('cell', models.PositiveIntegerField()),
            ],
        ),
    ]
