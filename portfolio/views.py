from django.shortcuts import get_object_or_404, render

from .models import (
    Award,
    Education,
    Experience,
    PortfolioProfile,
    Publication,
    ResearchProject,
    SkillCategory,
)


def home(request):
    profile = get_object_or_404(PortfolioProfile.objects.order_by("pk"))
    context = {
        "profile": profile,
        "education": Education.objects.all(),
        "experiences": Experience.objects.all(),
        "projects": ResearchProject.objects.all(),
        "publications": Publication.objects.all(),
        "skill_categories": SkillCategory.objects.prefetch_related("skills"),
        "awards": Award.objects.all(),
    }
    return render(request, "portfolio/home.html", context)
