<template>
  <div class="submit-form">
    <div v-if="!submitted">
      <br>
    <h4>New Delivery</h4>
      <table>
      <tr><td>
        <label for="parcel"> Status </label><br>
     </td><td>
        <select v-model="Delivery.status">
          <option v-for="status in this.statuses" :key="status.id" :value=status.id>
              {{status.name}}
          </option>
        </select>
    </td></tr>
      <tr><td>
        <label for="parcel"> Parcel </label>
     </td><td>
        <select v-model="Delivery.parcel">
          <option v-for="parcel in this.parcels" :key="parcel.id" :value=parcel.id>
              {{parcel.number}} {{parcel.delivery_address_data}}
          </option>
        </select>
    </td></tr>
      <tr><td>
        <label for="courier"> Courier </label><br>
     </td><td>
        <select v-model="Delivery.courier">
          <option v-for="courier in this.couriers" :key="courier.id" :value=courier.id>
              {{courier.name}} {{courier.last_name}}
          </option>
        </select>
    </td></tr>
      <tr><td>
        <label for="send_date"> Send date </label>
     </td><td>
        <input
          type="datetime-local"
          class="form-control"
          id="send_date"
          required
          v-model="Delivery.send_date"
          name="send_date"
        />
    </td></tr>
      <tr><td>
        <label for="delivery_date"> Delivery date </label>
     </td><td>
        <input
          type="datetime-local"
          class="form-control"
          id="delivery_date"
          required
          v-model="Delivery.delivery_date"
          name="delivery_date"
        />
    </td></tr>
    </table>
    <button @click="saveDelivery" class="btn btn-success">Submit</button>
    </div>
    <div v-else>
      <h4>You submitted successfully!</h4>
      <button class="btn btn-success" @click="newDelivery">Add</button>
    </div>
  </div>
</template>
<script>
import DeliveryDataService from '../services/DeliveryDataService';
import ParcelDataService from '../services/ParcelDataService';
import CourierDataService from '../services/CourierDataService';


export default {
  name: "add-Delivery",
  data() {
    return {
      couriers:null,
      parcels:null,
      statuses:null,
      Delivery: {
        id: null,
        parcel: null,
        send_date: null,
        delivery_date: null,
        courier: null,
        status:null
      },
      submitted: false
    };
  },
  methods: {
    saveDelivery() {
      var data = {
        status: this.Delivery.status,
        send_date: this.Delivery.send_date,
        delivery_date: this.Delivery.delivery_date,
        courier: this.Delivery.courier,
        parcel: this.Delivery.parcel,
      };
      DeliveryDataService.create(data)
        .then(response => {
          this.Delivery.id = response.data.id;
          console.log(response.data);
          this.submitted = true;
        })
        .catch(e => {
          console.log(e);
        });
    },
    newDelivery() {
      this.submitted = false;
      this.Delivery = {};
    },
    getCouriers() {
      CourierDataService.getAll()
        .then(response => {
          this.couriers = response.data;
        })
        .catch(e => {
          console.log(e);
        });
    },
    getParcels() {
      ParcelDataService.getAll()
        .then(response => {
          this.parcels = response.data;
        })
        .catch(e => {
          console.log(e);
        });
    },
  },
  mounted() {
    this.message = '';
    this.getCouriers();
    this.getParcels();
    this.statuses = [ {'id':1, 'name':'New'},  {'id':2, 'name':'Sending'},  {'id':3, 'name':'On way'}, {'id':4, 'name':'On delivery'}, {'id':5, 'name':'Delivered'}, {'id':6, 'name':'Not delivered'}];
  }

};


</script>
<style>
.submit-form {
  max-width: 300px;
  margin: auto;
}
</style>