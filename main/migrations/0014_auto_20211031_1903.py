# Generated by Django 3.2.8 on 2021-10-31 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_pagedocuments_pagedocumentsdocument_pagedocumentsdocumentimg'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300, verbose_name='Название')),
                ('company', models.CharField(choices=[('Rigel-Z', 'Rigel-Z'), ('ROSTERMINĀLS', 'ROSTERMINĀLS'), ('STRAUME', 'STRAUME')], default='Rigel-Z', max_length=30, verbose_name='Компания')),
                ('pdf', models.FileField(upload_to='pdf/', verbose_name='PDF')),
            ],
            options={
                'verbose_name': 'Страница - Документы',
                'verbose_name_plural': 'Страница - Документы',
            },
        ),
        migrations.CreateModel(
            name='PageDocumentImg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='document-img/', verbose_name='Изображение')),
                ('pageDocumentImg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documentImg', to='main.pagedocument')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
        migrations.RemoveField(
            model_name='pagedocumentsdocument',
            name='pageDocumentsDocument',
        ),
        migrations.RemoveField(
            model_name='pagedocumentsdocumentimg',
            name='pageDocumentsDocumentImg',
        ),
        migrations.AlterModelOptions(
            name='pagephotogalleryproject',
            options={},
        ),
        migrations.RemoveField(
            model_name='pagephotogalleryproject',
            name='img1',
        ),
        migrations.RemoveField(
            model_name='pagephotogalleryproject',
            name='img2',
        ),
        migrations.DeleteModel(
            name='PageDocuments',
        ),
        migrations.DeleteModel(
            name='PageDocumentsDocument',
        ),
        migrations.DeleteModel(
            name='PageDocumentsDocumentImg',
        ),
    ]
