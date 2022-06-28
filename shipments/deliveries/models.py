from django.db import models


class Courier(models.Model):
    name  =  models.CharField(max_length=64)
    last_name =  models.CharField(max_length=200)
    def __str__(self):
        return  '{} {}'.format(
            self.name,self.last_name)

class Address(models.Model):
    name = models.CharField(max_length=64)
    family_name = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    post_code = models.CharField(max_length=5)
    country = models.CharField(max_length=64)

    def __str__(self):
        return  'Name: {} {}, Street: {}, City: {}, Post code: {}, Country: {}'.format(
            self.family_name,self.name, self.street, self.city, self.post_code, self.country)


class Parcel(models.Model):
    number =  models.CharField(max_length=32, blank=True)
    delivery_address = models.ForeignKey(Address, on_delete=models.PROTECT, related_name='parcel_to_deliver')
    sender_address = models.ForeignKey(Address, on_delete=models.PROTECT, related_name='parcel_to_send')

    @property
    def sender_address_data(self):
        return str(self.sender_address)

    @property
    def delivery_address_data(self):
        return str(self.delivery_address)

class Delivery(models.Model):
    STATUS_NEW = 1
    STATUS_SENDING = 2
    STATUS_ON_WAY = 3
    STATUS_ON_DELIVERY = 4
    STATUS_DELIVERED = 5
    STATUS_NOT_DELIVERED = 6

    STATUS_CHOICES = (
        (STATUS_NEW,'New'),
        (STATUS_SENDING, 'Sending'),
        (STATUS_ON_WAY, 'On way'),
        (STATUS_ON_DELIVERY, 'On delivery'),
        (STATUS_DELIVERED, 'Deliveder'),
        (STATUS_NOT_DELIVERED, 'Not delivered'),
    )

    STATUS_TABLE = {
        STATUS_NEW:'New',
        STATUS_SENDING: 'Sending',
        STATUS_ON_WAY: 'On way',
        STATUS_ON_DELIVERY: 'On delivery',
        STATUS_DELIVERED: 'Deliveder',
        STATUS_NOT_DELIVERED: 'Not delivered'
    }

    status = models.IntegerField(choices=STATUS_CHOICES, default=STATUS_NEW)
    send_date = models.DateTimeField('date sended',  blank=True, null=True)
    delivery_date = models.DateTimeField('date delivered',  blank=True, null=True)
    parcel = models.ForeignKey(Parcel, on_delete=models.CASCADE)
    courier = models.ForeignKey(Courier,  on_delete=models.PROTECT)

    @property
    def parcel_sender_address_data(self):
        return str(self.parcel.sender_address)

    @property
    def parcel_delivery_address_data(self):
        return str(self.parcel.delivery_address)

    @property
    def courier_name(self):
        return str(self.courier)

    @property
    def parcel_number(self):
        return str(self.parcel.number)

    @property
    def status_name(self):
        return self.STATUS_TABLE[self.status]