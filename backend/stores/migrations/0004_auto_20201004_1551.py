# Generated by Django 3.1.2 on 2020-10-04 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0003_auto_20201003_1420'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='user',
        ),
        migrations.AddField(
            model_name='store',
            name='bigcategory',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
