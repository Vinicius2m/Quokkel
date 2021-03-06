# Generated by Django 4.0.4 on 2022-05-26 16:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('reservation_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('in_reservation_date', models.DateField()),
                ('out_reservation_date', models.DateField()),
                ('checkin_date', models.DateField(null=True)),
                ('checkout_date', models.DateField(null=True)),
                ('status', models.CharField(max_length=50)),
                ('total_value', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
            ],
        ),
    ]
