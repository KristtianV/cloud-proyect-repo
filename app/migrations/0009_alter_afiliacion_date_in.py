# Generated by Django 3.2.7 on 2021-11-28 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_implicado_charges'),
    ]

    operations = [
        migrations.AlterField(
            model_name='afiliacion',
            name='date_in',
            field=models.DateField(null=True),
        ),
    ]