<template>
  <div v-if="currentDelivery" class="edit-form">
    <h4>Delivery</h4>
    <form>
      <table>
        <tr><td>
        <label for="number">Status</label>
        </td><td>
        <select v-model="currentDelivery.status">
          <option v-for="status in this.statuses" :key="status.id" :value=status.id>
              {{status.name}}
          </option>
        </select>
        </td></tr>
        <tr><td>
        <label for="number">Send date</label>
        </td><td>
        <input type="datetime-local" class="form-control" id="send_date"
          v-model="currentDelivery.send_date"
        />
        </td></tr>
        <tr><td>
        <label for="number">Delivery date</label>
        </td><td>
        <input type="datetime-local" class="form-control" id="delivery_date"
          v-model="currentDelivery.delivery_date"
        />
        </td></tr>
        <tr><td>
        <label for="parcel">Parcel</label>
        </td><td>
        <select v-model="currentDelivery.parcel">
          <option v-for="parcel in this.parcels" :key="parcel.id" :value=parcel.id>
              {{parcel.number}} {{parcel.delivery_address}}
          </option>
        </select>
        </td></tr>
        <tr><td>
        <label for="courier">Courier</label>
        </td><td>
        <select v-model="currentDelivery.courier">
          <option v-for="courier in this.couriers" :key="courier.id" :value=courier.id>
              {{courier.name}} {{courier.lastname}}
          </option>
        </select>
        </td></tr>
       </table>
    </form>
    <button class="badge badge-danger mr-2"
      @click="deleteDelivery">
      Delete
    </button>
    <button type="submit" class="badge badge-success"
      @click="updateDelivery"
    >
      Update
    </button>
    <p>{{ message }}</p>
  </div>
  <div v-else>
    <br />
    <p>Please click on a Delivery...</p>
  </div>
</template>
<script>
import DeliveryDataService from '../services/DeliveryDataService';
import ParcelDataService from '../services/ParcelDataService';
import CourierDataService from '../services/CourierDataService';

export default {
  name: "Delivery-details",
  data() {
    return {
      currentDelivery: null,
      couriers: null,
      parcels: null,
      send_date: "",
      delivery_date: "",
      status: null,
    };
  },
  methods: {
    getDelivery(id) {
      DeliveryDataService.get(id)
        .then(response => {
          this.currentDelivery = response.data;
          this.currentDelivery.send_date=this.currentDelivery.send_date.substr(0, 16);
          this.currentDelivery.delivery_date=this.currentDelivery.delivery_date.substr(0, 16);
          console.log(response.data);
        })
        .catch(e => {
          console.log(e);
        });
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
    updateDelivery() {
      DeliveryDataService.update(this.currentDelivery.id, this.currentDelivery)
        .then(response => {
          console.log(response.data);
          this.message = 'The Delivery was updated successfully!';
        })
        .catch(e => {
          console.log(e);
        });
    },
    deleteDelivery() {
      DeliveryDataService.delete(this.currentDelivery.id)
        .then(response => {
          this.$router.push({ name: "Deliverys-list" }); console.log(response);
        })
        .catch(e => {
          console.log(e);
        });
    }
  },
  mounted() {
    this.message = '';
    this.getParcels();
    this.getCouriers();
    this.getDelivery(this.$route.params.id);
    this.statuses = [ {'id':1, 'name':'New'},  {'id':2, 'name':'Sending'},  {'id':3, 'name':'On way'}, {'id':4, 'name':'On delivery'}, {'id':5, 'name':'Delivered'}, {'id':6, 'name':'Not delivered'}];
  }
};
</script>
<style>
.edit-form {
  max-width: 300px;
  margin: auto;
}
</style>