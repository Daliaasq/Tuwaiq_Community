# Generated by Django 4.2.1 on 2023-06-14 20:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_user', models.CharField(blank=True, max_length=2048)),
                ('avatar', models.ImageField(default='images/bootstrap.png', upload_to='images/')),
                ('github_link', models.URLField(blank=True)),
                ('linkedin_link', models.URLField(blank=True)),
                ('twitter_link', models.URLField(blank=True)),
                ('bootcamp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.bootcamp')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
