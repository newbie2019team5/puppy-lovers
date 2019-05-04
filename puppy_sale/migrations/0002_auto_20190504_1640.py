# Generated by Django 2.1.8 on 2019-05-04 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puppy_sale', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='transactable_id',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='transaction',
            name='transactable_name',
            field=models.CharField(default='', max_length=30),
        ),
    ]