# Generated by Django 3.2.4 on 2021-09-29 00:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0004_pet_owners'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pet.petcategory'),
        ),
    ]
