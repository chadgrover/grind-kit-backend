# Generated by Django 4.1.3 on 2022-11-24 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grind_kit', '0012_rename_jobs_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instancecontent',
            name='name',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
