# Generated by Django 2.2.3 on 2019-08-01 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20190801_0724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='amount_views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]