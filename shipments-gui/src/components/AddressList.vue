<template>
  <div class="list row">
    <div class="col-md-12">
      <h4>Address List</h4>
        <router-link to="/addaddress" class="nav-link">New Address</router-link>
        <table class="table">
        <thead>
        <tr>
        <th scope="col">#</th>
        <th scope="col">Name</th>
        <th scope="col">Last name</th>
        <th scope="col">Street</th>
        <th scope="col">City</th>
        <th scope="col">Post code</th>
        <th scope="col">Country</th>
        <th> Action</th>
        </tr>
        </thead>
        <tbody>
        <template v-for="(Address, index) in Addresses" :key="index">
          <tr>
          <th scope="row">{{ Address.id }} </th>
          <td>{{ Address.name }}</td>
          <td>{{ Address.family_name }}</td>
          <td>{{ Address.street }}</td>
          <td>{{ Address.city }}</td>
          <td>{{ Address.post_code }}</td>
          <td>{{ Address.country }}</td>
          <td><router-link :to="'/Address/' + Address.id " class="badge badge-warning">Edit</router-link> </td>
        </tr>
      </template>
      </tbody>
      </table>
    </div>
  </div>
</template>
<script>

import AddressDataService from '../services/AddressDataService';

export default {
  name: "address-list",
  data() {
    return {
      Addresses: [],
      currentAddress: null,
      currentIndex: -1,
      number: ""
    };
  },
  methods: {
    retrieveAddresses() {
      AddressDataService.getAll()
        .then(response => {
          this.Addresses = response.data;
        })
        .catch(e => {
          console.log(e);
        });
    },
    refreshList() {
      this.retrieveAddresses();
      this.currentAddress = null;
      this.currentIndex = -1;
    },
  },
  mounted() {
    this.retrieveAddresses();
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