from django.contrib import admin

from .models import (
    Award,
    Education,
    Experience,
    PortfolioProfile,
    Publication,
    ResearchProject,
    Skill,
    SkillCategory,
)


@admin.register(PortfolioProfile)
class PortfolioProfileAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not PortfolioProfile.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("degree", "institution", "period", "display_order")
    list_editable = ("display_order",)
    search_fields = ("degree", "institution", "thesis")


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("role", "organization", "period", "display_order")
    list_editable = ("display_order",)
    search_fields = ("role", "organization", "summary", "highlights")


@admin.register(ResearchProject)
class ResearchProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "period", "display_order")
    list_editable = ("display_order",)
    list_filter = ("category",)
    search_fields = ("title", "description", "result")


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ("title", "year", "publication_type", "status", "display_order")
    list_filter = ("publication_type", "year")
    search_fields = ("title", "authors", "venue")


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1


@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "display_order")
    list_editable = ("display_order",)
    inlines = (SkillInline,)


@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ("title", "organization", "year", "display_order")
    list_editable = ("display_order",)
    search_fields = ("title", "organization", "details")


admin.site.site_header = "Mahedi Hasan — Portfolio content"
admin.site.site_title = "Portfolio administration"
admin.site.index_title = "Manage portfolio content"
