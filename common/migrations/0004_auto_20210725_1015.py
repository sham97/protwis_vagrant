# Generated by Django 3.0.3 on 2021-07-25 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_citation_page_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='web_link',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='common.WebLink'),
        ),
    ]
