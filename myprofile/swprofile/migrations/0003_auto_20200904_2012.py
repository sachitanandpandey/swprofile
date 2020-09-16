# Generated by Django 3.1.1 on 2020-09-04 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swprofile', '0002_auto_20200904_2001'),
    ]

    operations = [
        migrations.CreateModel(
            name='aboutus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aboutus', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='apps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('Domain', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameModel(
            old_name='Question',
            new_name='homemsg',
        ),
    ]
