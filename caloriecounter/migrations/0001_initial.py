# Generated by Django 3.0.6 on 2020-07-14 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('protein', models.IntegerField(default=0)),
                ('carbohydrates', models.IntegerField(default=0)),
                ('cholestrol', models.IntegerField(default=0)),
                ('fat', models.IntegerField(default=0)),
                ('fiber', models.IntegerField(default=0)),
                ('saturated_salt', models.IntegerField(default=0)),
            ],
        ),
    ]