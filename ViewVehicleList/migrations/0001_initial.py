# Generated by Django 2.2 on 2018-09-11 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CarBrand', models.CharField(default='Car Brand', max_length=32)),
                ('CarModel', models.CharField(default='Model', max_length=32)),
            ],
        ),
    ]
