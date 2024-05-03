from django.contrib import admin
from .models import BugReport, FeatureRequest


@admin.register(BugReport)
class BugAdmin(admin.ModelAdmin):
    fieldsets = [
            ('Main Information', {'fields': ['title', 'description', 'project', 'task']}),
            ('Additional Information', {'fields': ['status', 'priority']}),
        ]

    list_display = ('title', 'project', 'task', 'status', 'priority', 'created_at', 'updated_at')
    list_filter = ('task', 'status', 'priority', 'updated_at')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at', 'updated_at')
    list_editable = ('status',)


@admin.register(FeatureRequest)
class FeatureAdmin(admin.ModelAdmin):
    fieldsets = [
            ('Main Information', {'fields': ['title', 'description', 'project', 'task']}),
            ('Additional Information', {'fields': ['status', 'priority']}),
        ]
    list_display = ('title', 'project', 'task', 'status', 'priority', 'created_at', 'updated_at')
    list_filter = ('task', 'status', 'priority', 'updated_at')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at', 'updated_at')
    list_editable = ('status',)
