from django.contrib import admin
from .models import Book, Chapter

admin.site.site_header = "My Library Admin"  
# Register your models here.)  
@admin.register(Book)  
class BookAdmin(admin.ModelAdmin):  
    list_display = ('title', 'author', 'isPublished', 'ChapterName')  
    list_filter = ('isPublished',)  
    search_fields = ('title', 'author')  
    readonly_fields = ('published_date',)
    
