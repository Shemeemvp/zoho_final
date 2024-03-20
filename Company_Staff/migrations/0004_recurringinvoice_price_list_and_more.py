# Generated by Django 4.2.3 on 2024-03-20 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Company_Staff', '0003_recurring_invoice_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='recurringinvoice',
            name='price_list',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Company_Staff.pricelist'),
        ),
        migrations.AddField(
            model_name='recurringinvoice',
            name='price_list_applied',
            field=models.BooleanField(default=False, null=True),
        ),
    ]