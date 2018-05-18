# Generated by Django 2.0.4 on 2018-05-18 02:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AbstractOrder',
            fields=[
                ('order_type', models.CharField(blank=True, default='', max_length=10)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('QUOTE', 'QUOTE'), ('ORDER', 'ORDER'), ('COMPLETED', 'COMPLETED'), ('ARCHIVE', 'ARCHIVED')], max_length=10)),
                ('quote', models.IntegerField(default=0)),
                ('quote_date', models.DateField(blank=True, null=True)),
                ('order_date', models.DateField(blank=True, null=True)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('deposite', models.IntegerField(default=0)),
                ('final_price', models.IntegerField(default=0)),
                ('balance', models.IntegerField(default=0)),
                ('notes', models.TextField(blank=True, null=True)),
                ('need_approval', models.BooleanField(default=False)),
                ('approved', models.BooleanField(default=False)),
                ('payment_due_date', models.DateField(blank=True, null=True)),
                ('updated', models.DateField()),
                ('created', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='CustomerModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('company', models.CharField(blank=True, max_length=30, null=True)),
                ('phone', models.CharField(blank=True, max_length=13, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('address', models.CharField(blank=True, max_length=30, null=True)),
                ('city', models.CharField(blank=True, max_length=20, null=True)),
                ('zip', models.IntegerField(blank=True, null=True)),
                ('balance', models.IntegerField(blank=True, default=0)),
                ('last_in', models.DateField(blank=True, null=True)),
                ('folder_location', models.CharField(blank=True, max_length=80, null=True)),
                ('needs_followup', models.BooleanField(default=False)),
                ('updated', models.DateField(blank=True, null=True)),
                ('created', models.DateField(blank=True, null=True)),
                ('last_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PrintOrder',
            fields=[
                ('abstractorder_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='backend.AbstractOrder')),
                ('double_sided', models.BooleanField(default=False)),
                ('material_color', models.CharField(max_length=20)),
                ('weight', models.CharField(choices=[('20Lb', '20'), ('30Lb', '30'), ('50Lb', '50')], max_length=20)),
                ('size', models.CharField(max_length=20)),
                ('original_size', models.CharField(max_length=20)),
                ('quantity', models.IntegerField()),
                ('material', models.CharField(choices=[('CardStock', 'cardstock'), ('Gloss', 'gloss'), ('News', 'news')], max_length=20)),
                ('stapled', models.BooleanField(default=False)),
                ('padded', models.BooleanField(default=False)),
                ('folding', models.BooleanField(default=False)),
                ('collated', models.BooleanField(default=False)),
                ('scoring', models.BooleanField(default=False)),
            ],
            bases=('backend.abstractorder',),
        ),
        migrations.CreateModel(
            name='SignOrder',
            fields=[
                ('abstractorder_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='backend.AbstractOrder')),
                ('quantity', models.IntegerField()),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('material', models.CharField(max_length=40)),
                ('double_sided', models.BooleanField(default=False)),
                ('gromets', models.BooleanField(default=False)),
                ('sewing', models.BooleanField(default=False)),
                ('webbing', models.BooleanField(default=False)),
                ('tape', models.BooleanField(default=False)),
                ('corner_rounding', models.BooleanField(default=False)),
            ],
            bases=('backend.abstractorder',),
        ),
        migrations.AddField(
            model_name='abstractorder',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='abstractorder',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.CustomerModel'),
        ),
    ]
