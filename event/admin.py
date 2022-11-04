from django.contrib import admin
from django_admin_geomap import ModelAdmin
from .models import *

# Register your models here.
class Admin(ModelAdmin):
    geomap_field_longitude = "id_lon"
    geomap_field_latitude = "id_lat"

admin.site.register(Location, Admin)
admin.site.register(EventCategory)
admin.site.register(EventSponser)
admin.site.register(Event)
admin.site.register(EventImage)
admin.site.register(EventAgenda)
# admin.site.register(EventJobCategoryLinking)
admin.site.register(EventMember)
admin.site.register(EventUserWishList)
admin.site.register(UserPoint)



