# Generated by Django 3.2.4 on 2021-07-01 12:12

from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CareCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('icon', models.IntegerField(blank=True, default=1, null=True)),
                ('input_type', models.CharField(blank=True, choices=[('text', 'テキスト'), ('integer', '整数'), ('float', '小数点'), ('checkbox', 'チェックボックス')], max_length=16, null=True)),
                ('unit', models.CharField(blank=True, max_length=10, null=True)),
                ('is_daily_routine', models.BooleanField(blank=True, default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日')),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='pet_images')),
                ('gender', models.CharField(blank=True, choices=[('male', 'オス'), ('female', 'メス')], max_length=16, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('welcome_day', models.DateField(blank=True, null=True)),
                ('share_id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('is_heaven', models.BooleanField(blank=True, default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日')),
            ],
        ),
        migrations.CreateModel(
            name='PetCareLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('integer', models.IntegerField(blank=True, null=True)),
                ('float', models.FloatField(blank=True, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('checkbox', models.BooleanField(blank=True, default=False)),
                ('date_time', models.DateTimeField()),
                ('memo', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日')),
            ],
        ),
        migrations.CreateModel(
            name='PetOwnerGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日')),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pet.pet')),
            ],
        ),
    ]
