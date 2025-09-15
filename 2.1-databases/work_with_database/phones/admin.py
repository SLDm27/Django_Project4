from django.contrib import admin

from phones.models import Phone

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image', 'price', 'lte_exists', 'slug']
    list_filter = ['name', 'price']

