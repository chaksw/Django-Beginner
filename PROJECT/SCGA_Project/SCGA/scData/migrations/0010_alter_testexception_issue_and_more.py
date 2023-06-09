# Generated by Django 4.2.2 on 2023-06-21 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scData', '0009_alter_testexception_ucclassification_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testexception',
            name='issue',
            field=models.CharField(choices=[(' ', ' '), ('N', 'No'), ('Y', 'Yes')], default=' ', max_length=10, verbose_name='Issue'),
        ),
        migrations.AlterField(
            model_name='testexception',
            name='ucClassification',
            field=models.CharField(choices=[('PAS', 'Previously Analyzed Software'), ('TEL', 'Test Environment Limitation'), ('IT', 'Incomplete Test'), ('DeactCode', 'Deactivated Code'), ('DefenCode', 'Defensive Code'), ('RCM', 'Requirement-Code Mismatch'), (' ', ' '), ('other', 'Other')], default=' ', max_length=100, verbose_name='Class'),
        ),
        migrations.AlterField(
            model_name='testplan',
            name='level',
            field=models.CharField(choices=[('B', 'B'), ('C', 'C'), ('A', 'A')], default='A', max_length=2, verbose_name='Level'),
        ),
        migrations.AlterField(
            model_name='testplan',
            name='overSight',
            field=models.CharField(choices=[(' ', ' '), ('N', 'No'), ('Y', 'Yes')], default=' ', max_length=3),
        ),
        migrations.AlterField(
            model_name='testplan',
            name='site',
            field=models.CharField(choices=[('Kaluga', 'BARS-Kaluga(EDS)'), ('Hyderabad', 'Hyderabad(EDS)'), ('Shanghai', 'Shanghai(EDS)'), ('Tambov', 'BARS-Tambov'), ('Beijing', 'Beijing(EDS)'), ('Info-Tech', 'Info-Tech'), ('Kursk', 'BARS-Kursk(All Avionics)'), ('Puetro Rico', 'Puetro Rico'), ('Moscow', 'BARS-Moscow(All Avionics)'), ('Taganrog', 'BARS-Taganrog(EDS)'), ('Madurai', 'Madurai(EDS)'), ('Bangalire', 'Bangalire(EDS)')], max_length=100, verbose_name='Site'),
        ),
    ]
