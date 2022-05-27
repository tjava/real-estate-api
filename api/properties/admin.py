from django.contrib import admin

from .models import Property, PropertyViews


class PropertyAdmin(admin.ModelAdmin):
    list_display = ["title", "state", "advert_type", "property_type"]
    list_filter = ["advert_type", "property_type", "state"]


admin.site.register(Property, PropertyAdmin)
admin.site.register(PropertyViews)
