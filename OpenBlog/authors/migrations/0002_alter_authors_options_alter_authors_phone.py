# Generated by Django 5.1.4 on 2024-12-19 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='authors',
            options={'verbose_name': 'Author', 'verbose_name_plural': 'Authors'},
        ),
        migrations.AlterField(
            model_name='authors',
            name='phone',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
