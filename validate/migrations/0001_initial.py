# Generated by Django 3.2.4 on 2021-06-29 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('reqid', models.AutoField(db_column='req_id', primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=25)),
                ('lastname', models.CharField(max_length=25)),
                ('dob', models.CharField(max_length=15)),
                ('gender', models.CharField(max_length=10)),
                ('nationality', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('pincode', models.CharField(max_length=10)),
                ('qualification', models.CharField(max_length=10)),
                ('salary', models.IntegerField()),
                ('pannumber', models.CharField(max_length=12)),
            ],
        ),
    ]