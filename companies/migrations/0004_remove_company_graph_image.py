# Generated by Django 2.2.1 on 2019-09-28 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_auto_20190928_1352'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='graph_image',
        ),
    ]
