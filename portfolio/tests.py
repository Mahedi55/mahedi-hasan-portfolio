from django.core.management import call_command
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
