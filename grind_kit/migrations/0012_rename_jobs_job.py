# Generated by Django 4.1.3 on 2022-11-23 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grind_kit', '0011_rename_job_jobs_rename_job_id_account_jobs_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Jobs',
            new_name='Job',
        ),
    ]
