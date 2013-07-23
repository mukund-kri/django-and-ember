from django.contrib import admin
from simple.models import Project, Task


class ProjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(Project, ProjectAdmin)


class TaskAdmin(admin.ModelAdmin):
    pass

admin.site.register(Task, TaskAdmin)


