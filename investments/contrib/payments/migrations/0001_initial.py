# Generated by Django 3.2.10 on 2021-12-30 13:54

import uuid

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("tags", "0001_initial"),
        ("positions", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Payment",
            fields=[
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("recorded_on", models.DateField(verbose_name="Recorded on")),
                (
                    "tags",
                    models.ManyToManyField(
                        blank=True,
                        related_name="dividend_payments",
                        to="tags.Tag",
                        verbose_name="Tags",
                    ),
                ),
            ],
            options={
                "verbose_name": "Payment",
                "verbose_name_plural": "Payments",
            },
        ),
        migrations.CreateModel(
            name="InterestPayment",
            fields=[
                (
                    "payment_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="payments.payment",
                    ),
                ),
                (
                    "amount",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=12,
                        validators=[django.core.validators.MinValueValidator(0)],
                        verbose_name="Amount",
                    ),
                ),
                (
                    "notes",
                    models.CharField(blank=True, max_length=1024, verbose_name="Notes"),
                ),
                (
                    "position",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="interest_payments",
                        to="positions.position",
                    ),
                ),
            ],
            options={
                "verbose_name": "Interest Payment",
                "verbose_name_plural": "Interest Payments",
            },
            bases=("payments.payment",),
        ),
        migrations.CreateModel(
            name="DividendPayment",
            fields=[
                (
                    "payment_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="payments.payment",
                    ),
                ),
                (
                    "amount",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=12,
                        validators=[django.core.validators.MinValueValidator(0)],
                        verbose_name="Amount",
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("monthly", "Monthly"),
                            ("quarterly", "Quarterly"),
                            ("semiannual", "Semiannual"),
                            ("annual", "Annual"),
                            ("special", "Special"),
                        ],
                        max_length=254,
                        verbose_name="Type",
                    ),
                ),
                (
                    "notes",
                    models.CharField(blank=True, max_length=1024, verbose_name="Notes"),
                ),
                (
                    "position",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="dividend_payments",
                        to="positions.position",
                    ),
                ),
            ],
            options={
                "verbose_name": "Dividend Payment",
                "verbose_name_plural": "Dividend Payments",
            },
            bases=("payments.payment",),
        ),
    ]
