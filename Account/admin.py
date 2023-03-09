from django.contrib import admin
from .models import Account
# Register your models here.

class AccountsAdmin(admin.ModelAdmin):
    class Meta:
        model=Account
    list_display = ['__str__', 'email', 'First_name', 'Last_name','Is_staff','contact','Location','is_admin','Date']
    list_filter = ['Date','Is_staff']
    search_fields = ['email','First_name',]
    list_per_page = 20
    exclude = ('password',)

admin.site.register(Account,AccountsAdmin)
