# Generated by Django 4.2.2 on 2023-06-15 03:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scData', '0004_testplan_level_testplan_testexception'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testplan',
            name='level',
            field=models.CharField(blank=True, choices=[('A', 'A'), ('C', 'C'), ('B', 'B')], default='', max_length=50, null=True, verbose_name='Level'),
        ),
        migrations.AlterField(
            model_name='testplan',
            name='testException',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='scData.testexception', verbose_name='Test Exception'),
        ),
    ]
