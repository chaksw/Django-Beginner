# Generated by Django 4.2.2 on 2023-06-16 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scData', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testplan',
            name='level',
            field=models.CharField(blank=True, choices=[('C', 'C'), ('A', 'A'), ('B', 'B')], default='', max_length=50, null=True, verbose_name='Level'),
        ),
    ]