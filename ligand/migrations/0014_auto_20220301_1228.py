# Generated by Django 2.2.1 on 2022-03-01 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ligand', '0013_auto_20220225_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ligand',
            name='uniprot',
            field=models.CharField(max_length=35, null=True),
        ),
    ]
