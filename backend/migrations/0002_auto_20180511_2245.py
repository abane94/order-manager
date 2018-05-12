# Generated by Django 2.0.4 on 2018-05-12 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='abstractorder',
            name='final_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='abstractorder',
            name='balance',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='abstractorder',
            name='deposite',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='abstractorder',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='abstractorder',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='abstractorder',
            name='order_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='abstractorder',
            name='payment_due_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='abstractorder',
            name='quote',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='abstractorder',
            name='quote_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
