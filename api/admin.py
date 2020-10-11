from django.contrib import admin

from api.models import Customer, Deal


class DealAdmin(admin.ModelAdmin):
    list_display = ['get_customer', 'item', 'total', 'quantity']
    ordering = ['date']

    def get_customer(self, obj):
        return obj.customer.username


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['username']


admin.site.register(Deal, DealAdmin)
admin.site.register(Customer, CustomerAdmin)
