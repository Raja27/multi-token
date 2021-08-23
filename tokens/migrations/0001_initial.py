from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MultiToken",
            fields=[
                (
                    "key",
                    models.CharField(
                        max_length=40,
                        primary_key=True,
                        serialize=False,
                        verbose_name="Key",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created"),
                ),
            ],
            options={
                "verbose_name": "Multi Token",
                "verbose_name_plural": "Multi Tokens",
            },
        ),
    ]
