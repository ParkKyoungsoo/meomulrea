# Generated by Django 3.1.1 on 2020-09-28 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='bigcategory',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
