# Generated by Django 3.2.7 on 2021-11-28 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_implicado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='implicado',
            name='charges',
            field=models.CharField(max_length=45, null=True),
        ),
    ]
