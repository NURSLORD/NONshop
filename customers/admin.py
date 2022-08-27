from django.contrib import admin

# Register your models here.
from customers.models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'age', 'address']
    list_display_links = ['name', 'surname']
    list_per_page = 10
    search_fields = ['name', 'surname', 'address']
    list_editable = ['address']


admin.site.register(Customer, CustomerAdmin)

