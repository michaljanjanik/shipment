<template>
  <div class="list row">
    <div class="col-md-16">
      <h4>Delivery List</h4>
     <router-link to="/adddelivery" class="nav-link">New Delivery</router-link>
	<table class="table">
	<thead>
	<tr>
        <th scope="col">#</th>
        <th scope="col">Status</th>
        <th scope="col">Parcel number</th>
        <th scope="col">Parcel delivery address</th>
        <th scope="col">Parcel sender address</th>
        <th scope="col">Send date</th>
        <th scope="col">Delivery date</th>
        <th scope="col">Courier</th>
	<th> Action</th>
        </tr>
        </thead>
        <tbody>
	<template v-for="(Delivery, index) in Deliveries" :key="index">
        <tr>
          <th scope="row">{{ Delivery.id }} </th>
          <td>{{ Delivery.status_name }}</td>
          <td>{{ Delivery.parcel_number }}</td>
          <td> {{ Delivery.parcel_delivery_address_data }} </td>
          <td> {{ Delivery.parcel_sender_address_data }} </td>
          <td> {{ Delivery.send_date }} </td>
          <td> {{ Delivery.delivery_date }} </td>
          <td> {{ Delivery.courier_name }} </td>
          <td><router-link :to="'/Delivery/' + Delivery.id " class="badge badge-warning">Edit</router-link> </td>
        </tr>
      </template>
      </tbody>
      </table>
    </div>
  </div>
</template>
<script>

import DeliveryDataService from '../services/DeliveryDataService';

export default {
  name: "Delivery-list",
  data() {
    return {
      Deliveries: [],
      currentDelivery: null,
      currentIndex: -1,
      number: ""
    };
  },
  methods: {
    retrieveDeliveries() {
      DeliveryDataService.getAll()
        .then(response => {
          this.Deliveries = response.data;
        })
        .catch(e => {
          console.log(e);
        });
    },
    refreshList() {
      this.retrieveDeliveries();
      this.currentDelivery = null;
      this.currentIndex = -1;
    },
  },
  mounted() {
    this.retrieveDeliveries();
  }
};
</script>
<style>
.list {
  text-align: left;
  max-width: 750px;
  margin: auto;
}
</style>