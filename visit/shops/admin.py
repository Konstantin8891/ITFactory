from django.contrib import admin

from .models import Shop, Visit


class ShopAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'employee_name')
    search_fields = ('name',)


class VisitAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'date', 'shop_name', 'longitude', 'latitude', 'employee'
    )
    search_fields = ('shop__name', 'shop__employee__name')


admin.site.register(Shop, ShopAdmin)
admin.site.register(Visit, VisitAdmin)
