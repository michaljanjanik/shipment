from django.test import TestCase
from .models import Delivery, Address, Courier, Parcel


class PropertiesTestCase(TestCase):
    def setUp(self):
        c1 = Courier.objects.create(name="Teofil", last_name="Dambrowski")
        Courier.objects.create(name="Zdzislaw", last_name="Malinowski")
        a1 = Address.objects.create(
            name="Anna",
            family_name="Klepacka",
            street="Jerozolimskie 12",
            city="Warszawa",
            post_code="02345",
            country="Polska",
        )
        a2 = Address.objects.create(
            name="Adam",
            family_name="Rzegocki",
            street="Mickiewicz 12",
            city="Krakow",
            post_code="42545",
            country="Polska",
        )
        parcel = Parcel.objects.create(
            number="123123", delivery_address=a1, sender_address=a2
        )
        Delivery.objects.create(
            parcel=parcel,
            courier=c1,
            send_date="2022-01-01 00:00",
            delivery_date="2022-01-07 00:00",
            status=1,
        )

    def test_parcel_address(self):
        parcel = Parcel.objects.get(number="123123")
        self.assertEqual(
            parcel.sender_address_data,
            "Name: Rzegocki Adam, Street: Mickiewicz 12, City: Krakow, Post code: 42545, Country: Polska",
        )

    def test_delivery_address(self):
        parcel = Parcel.objects.get(number="123123")
        delivery = Delivery.objects.get(parcel=parcel)
        self.assertEqual(
            delivery.parcel_sender_address_data,
            "Name: Rzegocki Adam, Street: Mickiewicz 12, City: Krakow, Post code: 42545, Country: Polska",
        )
