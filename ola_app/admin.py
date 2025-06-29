from django.contrib import admin
from .models import Category, GalleryImage, UploadSession

# Register your models here.
class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 3

class UploadSessionAdmin(admin.ModelAdmin):
    inlines = [GalleryImageInline]
    list_display = ['title', 'created_at']


admin.site.register(Category)
admin.site.register(UploadSession, UploadSessionAdmin)
