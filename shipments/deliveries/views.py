from .models import Address, Courier, Delivery, Parcel
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import (
    AddressSerializer,
    CourierSerializer,
    DeliverySerializer,
    ParcelSerializer,
)


class AddressViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Address.objects.all()
    serializer_class = AddressSerializer


#    permission_classes = [permissions.IsAuthenticated]


class CourierViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Courier.objects.all()
    serializer_class = CourierSerializer


#    permission_classes = [permissions.IsAuthenticated]


class DeliveryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer


#    permission_classes = [permissions.IsAuthenticated]


class ParcelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer


#    permission_classes = [permissions.IsAuthenticated]
