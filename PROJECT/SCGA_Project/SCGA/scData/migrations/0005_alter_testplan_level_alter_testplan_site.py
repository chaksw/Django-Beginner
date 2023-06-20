# Generated by Django 4.2.2 on 2023-06-20 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scData', '0004_alter_testexception_swline_alter_testplan_level_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testplan',
            name='level',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], default='A', max_length=2, verbose_name='Level'),
        ),
        migrations.AlterField(
            model_name='testplan',
            name='site',
            field=models.CharField(choices=[('Kaluga', 'BARS-Kaluga(EDS)'), ('Shanghai', 'Shanghai(EDS)'), ('Beijing', 'Beijing(EDS)'), ('Kursk', 'BARS-Kursk(All Avionics)'), ('Madurai', 'Madurai(EDS)'), ('Bangalire', 'Bangalire(EDS)'), ('Info-Tech', 'Info-Tech'), ('Taganrog', 'BARS-Taganrog(EDS)'), ('Hyderabad', 'Hyderabad(EDS)'), ('Puetro Rico', 'Puetro Rico'), ('Moscow', 'BARS-Moscow(All Avionics)'), ('Tambov', 'BARS-Tambov')], max_length=100, verbose_name='Site'),
        ),
    ]
