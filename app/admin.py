from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Projects)
class projectModelAdmin(admin.ModelAdmin):
    list_display = ['id','image']

@admin.register(Products)
class productModelAdmin(admin.ModelAdmin):
    list_display = ['id','typeOfProduct','description','imagebw1','imageclr2','image3','image4']