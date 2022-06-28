<template>
  <div class="list row">
    <div class="col-md-12">
      <h4>Parcels List</h4>
        <router-link to="/addparcel" class="nav-link">New Parcel</router-link>
	<table class="table">
	<thead>
	<tr>
        <th scope="col">#</th>
        <th scope="col">Number</th>
        <th scope="col">Sender address</th>
        <th scope="col">Delivery address</th>
	<th> Action</th>
        </tr>
        </thead>
        <tbody>
	<template v-for="(Parcel, index) in Parcels" :key="index">
        <tr>
          <th scope="row">{{ Parcel.id }} </th>
          <td>{{ Parcel.number }}</td>
          <td>{{ Parcel.sender_address_data }}</td>
          <td> {{ Parcel.delivery_address_data }} </td>
          <td><router-link :to="'/Parcel/' + Parcel.id " class="badge badge-warning">Edit</router-link> </td>
        </tr>
      </template>
      </tbody>
      </table>
    </div>
  </div>
</template>
<script>

import ParcelDataService from '../services/ParcelDataService';

export default {
  name: "parcels-list",
  data() {
    return {
      Parcels: [],
      currentParcel: null,
      currentIndex: -1,
      number: ""
    };
  },
  methods: {
    retrieveParcels() {
      ParcelDataService.getAll()
        .then(response => {
          this.Parcels = response.data;
          console.log(response.data);
        })
        .catch(e => {
          console.log(e);
        });
    },
    refreshList() {
      this.retrieveParcels();
      this.currentParcel = null;
      this.currentIndex = -1;
    },
  },
  mounted() {
    this.retrieveParcels();
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