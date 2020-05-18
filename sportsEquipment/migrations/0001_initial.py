# Generated by Django 2.1.7 on 2019-04-17 05:57

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EquipmentRequest',
            fields=[
                ('reqId', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(2)])),
                ('dtOfRequest', models.DateTimeField()),
                ('dtAvailed', models.DateTimeField(null=True)),
                ('dtOfExpRet', models.DateTimeField(null=True)),
                ('dtOfActualRet', models.DateTimeField(null=True)),
                ('penalty', models.IntegerField(default=0)),
                ('reqStatus', models.IntegerField(choices=[(0, 'PENDING'), (1, 'ACCEPTED'), (2, 'REJECTED'), (3, 'RETURNED')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Equipments',
            fields=[
                ('eqpId', models.AutoField(primary_key=True, serialize=False)),
                ('eqpName', models.CharField(max_length=50)),
                ('eqpQuantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('eqpQuantityTaken', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(models.IntegerField(validators=[django.core.validators.MinValueValidator(1)]))])),
            ],
        ),
        migrations.AddField(
            model_name='equipmentrequest',
            name='eqp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sportsEquipment.Equipments'),
        ),
        migrations.AddField(
            model_name='equipmentrequest',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
