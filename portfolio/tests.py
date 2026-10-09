import os
from unittest.mock import patch

from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.core.management.base import CommandError
from django.test import TestCase, override_settings

from .models import PortfolioProfile, Publication


@override_settings(
    STORAGES={
        "default": {"BACKEND": "django.core.files.storage.FileSystemStorage"},
        "staticfiles": {
            "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage"
        },
    }
)
class PortfolioHomeTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        call_command("seed_portfolio", verbosity=0)

    def test_homepage_renders_seeded_profile_and_sections(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Mahedi Hasan")
        self.assertContains(response, "Human-Centric Computer Vision")
        self.assertContains(response, "Selected publications")
        self.assertGreaterEqual(Publication.objects.count(), 8)

    def test_homepage_content_can_be_edited_in_database(self):
        profile = PortfolioProfile.objects.get(pk=1)
        profile.title = "Associate Professor"
        profile.save()

        response = self.client.get("/")

        self.assertContains(response, "Associate Professor")

    def test_admin_is_available(self):
        response = self.client.get("/admin/login/")

        self.assertEqual(response.status_code, 200)


class BootstrapPortfolioAdminTests(TestCase):
    environment_keys = (
        "PORTFOLIO_ADMIN_USERNAME",
        "PORTFOLIO_ADMIN_EMAIL",
        "PORTFOLIO_ADMIN_PASSWORD",
    )

    def test_creates_admin_once_without_resetting_password(self):
        env = {
            "PORTFOLIO_ADMIN_USERNAME": "portfolio-owner",
            "PORTFOLIO_ADMIN_EMAIL": "owner@example.com",
            "PORTFOLIO_ADMIN_PASSWORD": "A-long-unique-passphrase-for-portfolio-2026!",
        }

        with patch.dict(os.environ, env):
            call_command("bootstrap_portfolio_admin", verbosity=0)
            os.environ["PORTFOLIO_ADMIN_PASSWORD"] = "A-different-long-passphrase-2026!"
            call_command("bootstrap_portfolio_admin", verbosity=0)

        user = get_user_model().objects.get(username="portfolio-owner")
        self.assertTrue(user.is_superuser)
        self.assertTrue(
            user.check_password("A-long-unique-passphrase-for-portfolio-2026!")
        )

    def test_requires_credentials_until_an_admin_exists(self):
        with patch.dict(os.environ, {}, clear=False):
            for key in self.environment_keys:
                os.environ.pop(key, None)

            with self.assertRaises(CommandError):
                call_command("bootstrap_portfolio_admin", verbosity=0)

    def test_missing_bootstrap_credentials_are_safe_after_admin_creation(self):
        user_model = get_user_model()
        user_model.objects.create_superuser(
            username="existing-owner",
            email="existing@example.com",
            password="A-long-unique-passphrase-for-existing-owner-2026!",
        )

        with patch.dict(os.environ, {}, clear=False):
            for key in self.environment_keys:
                os.environ.pop(key, None)
            call_command("bootstrap_portfolio_admin", verbosity=0)
