# Generated by Django 3.2.8 on 2021-10-23 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20211023_1418'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pagecontactspeople',
            name='photo',
        ),
        migrations.AddField(
            model_name='pagecontactspeople',
            name='name',
            field=models.CharField(blank=True, max_length=300, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='pagecontactspeople',
            name='post',
            field=models.CharField(blank=True, max_length=300, verbose_name='Должность'),
        ),
    ]