# Generated by Django 3.2.4 on 2021-06-28 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='share_id',
            field=models.CharField(blank=True, default='WtPGOvYzUvhy4IfB9qMIVsY0igFNKYCmObHmSwPMfjcNKCzCGu', max_length=128, unique=True),
        ),
    ]
