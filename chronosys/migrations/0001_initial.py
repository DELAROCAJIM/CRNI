# Generated by Django 4.0.3 on 2022-05-12 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChronoBreak_form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chrono_name', models.TextField(default='nice_guy')),
                ('chrono_email', models.TextField(blank=True)),
                ('chrono_inquiry', models.TextField(blank=True)),
                ('chrono_contact', models.TextField(blank=True)),
                ('chrono_message', models.TextField(blank=True)),
            ],
        ),
    ]
