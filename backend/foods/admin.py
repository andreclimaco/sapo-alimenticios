from django.contrib import admin
from .models import Food

# Register your models here.

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'quantity',
        'proteins',
        'carbohydrates',
        'fats',
        'created_at',
        'updated_at',
        'active'
    )