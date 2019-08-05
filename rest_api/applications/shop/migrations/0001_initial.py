# Generated by Django 2.2.3 on 2019-08-05 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('description', models.TextField(blank=True, max_length=255)),
                ('amount_items', models.IntegerField(blank=True, default=0)),
                ('amount_inner_categories', models.IntegerField(blank=True, default=0)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('price', models.FloatField()),
                ('description', models.TextField(blank=True, max_length=255)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('amount_views', models.PositiveIntegerField(default=0)),
                ('published', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.Category')),
            ],
        ),
    ]
