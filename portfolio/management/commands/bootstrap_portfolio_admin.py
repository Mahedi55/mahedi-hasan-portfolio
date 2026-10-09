import os

from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Create the initial portfolio administrator from environment variables."

    def handle(self, *args, **options):
        user_model = get_user_model()
        username = os.getenv("PORTFOLIO_ADMIN_USERNAME", "").strip()

        if not username:
            if user_model.objects.filter(is_superuser=True).exists():
                self.stdout.write("An administrator already exists; skipping bootstrap.")
                return
            raise CommandError(
                "Set PORTFOLIO_ADMIN_USERNAME, PORTFOLIO_ADMIN_EMAIL, and "
                "PORTFOLIO_ADMIN_PASSWORD to create the initial administrator."
            )

        user = user_model.objects.filter(username=username).first()
        if user:
            if not user.is_superuser:
                raise CommandError(
                    f"The account {username!r} exists but is not an administrator."
                )
            self.stdout.write("The configured administrator already exists; no changes made.")
            return

        email = os.getenv("PORTFOLIO_ADMIN_EMAIL", "").strip()
        password = os.getenv("PORTFOLIO_ADMIN_PASSWORD", "")
        missing = [
            name
            for name, value in (
                ("PORTFOLIO_ADMIN_EMAIL", email),
                ("PORTFOLIO_ADMIN_PASSWORD", password),
            )
            if not value
        ]
        if missing:
            raise CommandError(
                "Set the following environment variables to create the initial "
                f"administrator: {', '.join(missing)}."
            )

        candidate = user_model(username=username, email=email)
        try:
            validate_password(password, candidate)
        except ValidationError as error:
            raise CommandError(
                "PORTFOLIO_ADMIN_PASSWORD does not satisfy the configured password "
                f"policy: {'; '.join(error.messages)}"
            ) from error

        user_model.objects.create_superuser(
            username=username,
            email=email,
            password=password,
        )
        self.stdout.write(self.style.SUCCESS("Created the initial portfolio administrator."))
