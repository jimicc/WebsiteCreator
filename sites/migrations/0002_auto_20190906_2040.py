# Generated by Django 2.2 on 2019-09-06 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cards',
            name='image',
            field=models.FileField(blank=True, default='hills.png', upload_to=''),
        ),
    ]
