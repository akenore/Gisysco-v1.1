# Generated by Django 3.2.16 on 2022-12-01 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_auto_20221201_0726'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='company_vat',
            field=models.CharField(default=22, max_length=200, verbose_name='Company VAT'),
            preserve_default=False,
        ),
    ]