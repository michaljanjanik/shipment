from .models import Address, Courier, Delivery, Parcel
from rest_framework import serializers


class ParcelSerializer(serializers.ModelSerializer):
    delivery_address_data = serializers.ReadOnlyField()
    sender_address_data = serializers.ReadOnlyField()
    class Meta:
        model = Parcel
        fields = ['id','number', 'delivery_address', 'sender_address', 'delivery_address_data','sender_address_data']

class DeliverySerializer(serializers.ModelSerializer):
    parcel_delivery_address_data = serializers.ReadOnlyField()
    parcel_sender_address_data = serializers.ReadOnlyField()
    parcel_number = serializers.ReadOnlyField()
    courier_name = serializers.ReadOnlyField()
    status_name = serializers.ReadOnlyField()

    class Meta:
        model = Delivery
        fields = ['id','status','send_date','delivery_date','parcel','courier','status_name','parcel_number','courier_name', 'parcel_delivery_address_data','parcel_sender_address_data']

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id','name','family_name','street','city','post_code','country']

class CourierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courier
        fields = '__all__'

