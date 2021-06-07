# Generated by Django 3.1.5 on 2021-06-07 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20210604_1523'),
    ]

    operations = [
        migrations.CreateModel(
            name='partsName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reqPartName', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='serviceModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerRefId', models.CharField(max_length=10)),
                ('attendTech', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.techname')),
                ('parts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.partsname')),
            ],
        ),
    ]
