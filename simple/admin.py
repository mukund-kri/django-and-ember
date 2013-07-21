from django.contrib import admin
from simple.models import Project


class ProjectAdmin(admin.ModelAdmin):
    pass


admin.site.register(Project, ProjectAdmin)

