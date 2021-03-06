# Generated by Django 2.2 on 2020-03-28 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BeerDiaryItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beer_name', models.CharField(max_length=50)),
                ('brewer', models.CharField(max_length=50)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('price', models.FloatField(blank=True, default=0.0, null=True)),
                ('serving_type', models.IntegerField(choices=[(0, 'Bottle'), (1, 'Draft')], default=0)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
    ]
