# Generated by Django 3.2.12 on 2024-02-09 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20240209_1201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='otp',
            name='description',
        ),
        migrations.RemoveField(
            model_name='otp',
            name='name',
        ),
        migrations.RemoveField(
            model_name='otp',
            name='uuid',
        ),
        migrations.AddField(
            model_name='otp',
            name='code',
            field=models.CharField(default=123456, editable=False, max_length=6, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='otp',
            name='id',
            field=models.BigAutoField(auto_created=True, default=123456, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
