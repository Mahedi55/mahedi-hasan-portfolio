from django.db import models


class PortfolioProfile(models.Model):
    name = models.CharField(max_length=120)
    title = models.CharField(max_length=180)
    department = models.CharField(max_length=180)
    institution = models.CharField(max_length=180)
    location = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=40, blank=True)
    biography = models.TextField()
    research_interests = models.TextField(
        help_text="Enter one research interest per line."
    )
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    orcid_url = models.URLField(blank=True)
    scholar_url = models.URLField(blank=True)

    class Meta:
        verbose_name = "portfolio profile"
        verbose_name_plural = "portfolio profile"

    def __str__(self):
        return self.name

    @property
    def interests(self):
        return [item.strip() for item in self.research_interests.splitlines() if item.strip()]


class Education(models.Model):
    degree = models.CharField(max_length=180)
    institution = models.CharField(max_length=220)
    location = models.CharField(max_length=150)
    period = models.CharField(max_length=80)
    result = models.CharField(max_length=180, blank=True)
    thesis = models.CharField(max_length=300, blank=True)
    display_order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["display_order", "-period"]

    def __str__(self):
        return f"{self.degree} — {self.institution}"


class Experience(models.Model):
    role = models.CharField(max_length=180)
    organization = models.CharField(max_length=220)
    location = models.CharField(max_length=150)
    period = models.CharField(max_length=80)
    summary = models.TextField()
    highlights = models.TextField(
        help_text="Enter one achievement or responsibility per line."
    )
    display_order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["display_order", "-id"]
        verbose_name_plural = "experiences"

    def __str__(self):
        return f"{self.role} — {self.organization}"

    @property
    def highlight_items(self):
        return [item.strip() for item in self.highlights.splitlines() if item.strip()]


class ResearchProject(models.Model):
    title = models.CharField(max_length=240)
    category = models.CharField(max_length=100)
    period = models.CharField(max_length=80)
    description = models.TextField()
    result = models.CharField(max_length=300, blank=True)
    outcome = models.CharField(max_length=180, blank=True)
    display_order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["display_order", "-id"]

    def __str__(self):
        return self.title


class Publication(models.Model):
    class Type(models.TextChoices):
        JOURNAL = "journal", "Journal article"
        CONFERENCE = "conference", "Conference paper"
        BOOK_CHAPTER = "book_chapter", "Book chapter"

    title = models.CharField(max_length=400)
    authors = models.CharField(max_length=500)
    venue = models.CharField(max_length=300)
    year = models.PositiveSmallIntegerField()
    publication_type = models.CharField(max_length=20, choices=Type.choices)
    status = models.CharField(max_length=100, blank=True)
    doi_url = models.URLField(blank=True)
    display_order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["-year", "display_order", "title"]

    def __str__(self):
        return f"{self.title} ({self.year})"


class SkillCategory(models.Model):
    name = models.CharField(max_length=120)
    display_order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["display_order", "name"]
        verbose_name_plural = "skill categories"

    def __str__(self):
        return self.name


class Skill(models.Model):
    category = models.ForeignKey(
        SkillCategory, related_name="skills", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    display_order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["display_order", "name"]

    def __str__(self):
        return self.name


class Award(models.Model):
    title = models.CharField(max_length=220)
    organization = models.CharField(max_length=220)
    year = models.CharField(max_length=40)
    details = models.TextField(blank=True)
    display_order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["display_order", "-id"]

    def __str__(self):
        return f"{self.title} ({self.year})"
