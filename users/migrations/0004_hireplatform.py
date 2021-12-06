# Generated by Django 2.2.7 on 2019-12-21 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='HirePlatform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform_title', models.CharField(max_length=100)),
                ('platform_description', models.TextField(blank=True)),
                ('platform_profile_link', models.CharField(max_length=100)),
                ('platform_hire_link', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.Profile')),
            ],
        ),
    ]
