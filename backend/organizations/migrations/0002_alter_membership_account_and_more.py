# Generated by Django 5.0.3 on 2024-03-22 23:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_account_email_alter_account_password'),
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memberships', to='accounts.account'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memberships', to='organizations.organization'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='role',
            field=models.CharField(blank=True, choices=[('member', 'Member'), ('admin', 'Admin')], max_length=50),
        ),
        migrations.AlterField(
            model_name='organization',
            name='description',
            field=models.TextField(help_text='Enter a brief description of the organization'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='location',
            field=models.CharField(help_text="Enter the organization's location", max_length=100),
        ),
        migrations.AlterField(
            model_name='organization',
            name='members',
            field=models.ManyToManyField(related_name='organizations', through='organizations.Membership', to='accounts.account'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='name',
            field=models.CharField(help_text="Enter the organization's name", max_length=100),
        ),
    ]
