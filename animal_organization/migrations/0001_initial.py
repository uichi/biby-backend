# Generated by Django 3.2.4 on 2021-06-15 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('address', models.CharField(max_length=256, null=True)),
                ('phone_number', models.CharField(max_length=16, null=True)),
                ('home_page', models.CharField(max_length=256, null=True)),
            ],
        ),
    ]