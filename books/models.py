from django.db import models
from django.contrib import admin

class Book(models.Model):  
    title = models.CharField(max_length=100)  
    author = models.CharField(max_length=100)
    isPublished = models.BooleanField(default=False)
    published_date = models.DateTimeField  
    ChapterName = models.CharField(max_length=150)

class Chapter(models.Model):
    Name = models.ForeignKey(Book, on_delete=models.CASCADE)




class ChapterInline(admin.TabularInline):  # or StackedInline  
    model = Chapter  
    extra = 1  # Number of empty forms to display  

class BookAdmin(admin.ModelAdmin):  
    inlines = [ChapterInline]  