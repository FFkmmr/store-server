# Generated by Django 3.2.25 on 2024-06-01 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name': 'News', 'verbose_name_plural': 'News'},
        ),
        migrations.RemoveField(
            model_name='articles',
            name='article',
        ),
        migrations.AddField(
            model_name='articles',
            name='full_text',
            field=models.TextField(default='Empty', verbose_name='Full content'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='articles',
            name='anons',
            field=models.CharField(max_length=150, verbose_name='Anons'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='date',
            field=models.DateTimeField(verbose_name='Date of publication'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Title'),
        ),
    ]
