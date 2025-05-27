from django.contrib import admin
from .models import Project, Resume, Contact, Profile

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'technologies', 'created_at', 'updated_at')
    list_filter = ('created_at', 'technologies')
    search_fields = ('title', 'description', 'technologies')
    date_hierarchy = 'created_at'

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at')
    list_filter = ('uploaded_at',)
    search_fields = ('title',)
    date_hierarchy = 'uploaded_at'

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('created_at',)
    date_hierarchy = 'created_at'

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at', 'updated_at')
    search_fields = ('name', 'bio', 'email')
    readonly_fields = ('created_at', 'updated_at')

    def has_add_permission(self, request):
        # Only allow one profile instance
        if self.model.objects.exists():
            return False
        return True
