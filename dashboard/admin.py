from django.contrib import admin
from .models import Tools, Training_video  # Import your models
from django.utils.html import format_html  # Import for formatting HTML

# Custom admin class for Tools model
class ToolsAdmin(admin.ModelAdmin):
    list_display = ('tool_id', 'name', 'Category', 'License', 'Platforms')
    search_fields = ('name', 'Category', 'License', 'Platforms')
    list_filter = ('Category', 'License', 'Platforms')

# Custom admin class for Training_video model
class Training_videoAdmin(admin.ModelAdmin):
    list_display = ('Video_id', 'Title', 'pdf_field', 'Category', 'Skill_levels', 'descriptions', 'Video_URL')
    search_fields = ('Title', 'Category', 'Skill_levels')
    list_filter = ('Category', 'Skill_levels')

    def pdf_field(self, obj):
        # Display a link to the PDF if it exists
        if obj.pdf_field:
            return format_html('<a href="{}" target="_blank">View PDF</a>', obj.pdf_field.url)
        return "No PDF"
    
    pdf_field.short_description = 'PDF Link'

# Register your models and custom admin classes
admin.site.register(Tools, ToolsAdmin)
admin.site.register(Training_video, Training_videoAdmin)
