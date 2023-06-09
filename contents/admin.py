from django.contrib import admin
from contents.models import Section, Content
# Register your models here.

class SectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'caption')

class ContentAdmin(admin.ModelAdmin):
    list_display = ('section', 'title', 'details', 'image', 'status')

admin.site.register(Section, SectionAdmin)

admin.site.register(Content, ContentAdmin)
