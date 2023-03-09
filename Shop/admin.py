from django.contrib import admin
from .models import Shop_categories

# Register your models here.
class AccountsAdmin(admin.ModelAdmin):
    class Meta:
        model=Shop_categories
    list_display = ['__str__', 'Name_of_categories', 'Copune_code']
    list_filter = ['Name_of_categories','Copune_code']
    search_fields = ['Name_of_categories','Copune_code',]
    list_per_page = 20

admin.site.register(Shop_categories,AccountsAdmin)