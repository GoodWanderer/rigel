# Generated by Django 3.2.8 on 2021-10-31 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_pagehomeslider'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageDocuments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Страница - Документы',
                'verbose_name_plural': 'Страница - Документы',
            },
        ),
        migrations.CreateModel(
            name='PageDocumentsDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300, verbose_name='Название')),
                ('company', models.CharField(choices=[('Rigel-Z', 'Rigel-Z'), ('ROSTERMINĀLS', 'ROSTERMINĀLS'), ('STRAUME', 'STRAUME')], default='Rigel-Z', max_length=30, verbose_name='Компания')),
                ('pdf', models.FileField(upload_to='pdf/', verbose_name='PDF')),
                ('pageDocumentsDocument', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documentsDocument', to='main.pagedocuments')),
            ],
            options={
                'verbose_name': 'Документ',
                'verbose_name_plural': 'Докумнты',
            },
        ),
        migrations.CreateModel(
            name='PageDocumentsDocumentImg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='document-img/', verbose_name='Изображение')),
                ('pageDocumentsDocumentImg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documentsDocumentImg', to='main.pagedocumentsdocument')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
    ]
