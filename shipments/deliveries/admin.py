from django.contrib import admin
from .models import ( Address, Courier, Delivery, Parcel)

# Register your models here.
@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    pass

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass

@admin.register(Courier)
class CourierAdmin(admin.ModelAdmin):
    pass

@admin.register(Parcel)
class ParcelAdmin(admin.ModelAdmin):
    pass
