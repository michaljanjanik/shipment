<template>
  <div class="list row">
    <div class="col-md-12">
      <router-link to="/addcourier" class="nav-link">New Courier</router-link>
      <h4>Courier List</h4>
	<table class="table">
	<thead>
	<tr>
        <th scope="col">#</th>
        <th scope="col">Name</th>
        <th scope="col">Last name</th>
	<th> Action</th>
        </tr>
        </thead>
        <tbody>
	<template v-for="(Courier, index) in Couriers" :key="index">
        <tr>
          <th scope="row">{{ Courier.id }} </th>
          <td>{{ Courier.name }}</td>
          <td>{{ Courier.last_name }}</td>
          <td><router-link :to="'/Courier/' + Courier.id " class="badge badge-warning">Edit</router-link> </td>
        </tr>
      </template>
      </tbody>
      </table>
    </div>
  </div>
</template>
<script>

import CourierDataService from '../services/CourierDataService';

export default {
  name: "couriers-list",
  data() {
    return {
      Couriers: [],
      currentCourier: null,
      currentIndex: -1,
      number: ""
    };
  },
  methods: {
    retrieveCouriers() {
      CourierDataService.getAll()
        .then(response => {
          this.Couriers = response.data;
        })
        .catch(e => {
          console.log(e);
        });
    },
    refreshList() {
      this.retrieveCouriers();
      this.currentCourier = null;
      this.currentIndex = -1;
    },
  },
  mounted() {
    this.retrieveCouriers();
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