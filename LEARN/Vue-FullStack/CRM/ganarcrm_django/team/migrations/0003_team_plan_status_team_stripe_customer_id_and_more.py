# Generated by Django 4.2.3 on 2023-08-25 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_plan_team_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='plan_status',
            field=models.CharField(choices=[('active', 'Active'), ('cancelled', 'Cancelled')], default='active', max_length=20),
        ),
        migrations.AddField(
            model_name='team',
            name='stripe_customer_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='stripe_subscription_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
