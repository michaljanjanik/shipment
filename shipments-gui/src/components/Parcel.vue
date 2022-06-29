<template>
  <div v-if="currentParcel" class="edit-form">
    <h4>Parcel</h4>
    <form>
      <table>
        <tr><td>
        <label for="number"> Number&nbsp;&nbsp; </label>
        </td><td>
        <input type="text" class="form-control" id="number"
          v-model="currentParcel.number"
        />
        </td></tr>
        <tr><td>
        <label for="sender_address"> Sender address&nbsp;&nbsp; </label>
        </td><td>
        <select v-model="currentParcel.sender_address">
          <option v-for="address in this.addresses" :key="address.id" :value=address.id>
              {{address.name}} {{address.lastname}}  {{address.street }}  {{address.city }}  {{address.post_code }}  {{address.country }}
          </option>
        </select>
        </td></tr>
        <tr><td>
        <label for="sender_address"> Delivery address&nbsp;&nbsp; </label>
        </td><td>
        <select v-model="currentParcel.delivery_address">
          <option v-for="address in this.addresses" :key="address.id" :value=address.id>
              {{address.name}} {{address.lastname}}  {{address.street }}  {{address.city }}  {{address.post_code }}  {{address.country }}
          </option>
        </select>
        </td></tr>
      </table>
    </form>
    <button class="badge badge-danger mr-2"
      @click="deleteParcel">
      Delete
    </button>
    <button type="submit" class="badge badge-success"
      @click="updateParcel"
    >
      Update
    </button>
    <p>{{ message }}</p>
  </div>
  <div v-else>
    <br />
    <p>Please click on a Parcel...</p>
  </div>
</template>
<script>
import ParcelDataService from '../services/ParcelDataService';
import AddressDataService from '../services/AddressDataService';

export default {
  name: "parcel-details",
  data() {
    return {
      currentParcel: null,
      addresses: null,
      number: ""
    };
  },
  methods: {
    getParcel(id) {
      ParcelDataService.get(id)
        .then(response => {
          this.currentParcel = response.data;
        })
        .catch(e => {
          console.log(e);
        });
    },
    getAddresses() {
      AddressDataService.getAll()
        .then(response => {
          this.addresses = response.data;
        })
        .catch(e => {
          console.log(e);
        });
    },
    updateParcel() {
      ParcelDataService.update(this.currentParcel.id, this.currentParcel)
        .then(response => {
          this.message = 'The Parcel was updated successfully!';
        })
        .catch(e => {
          console.log(e);
        });
    },
    deleteParcel() {
      ParcelDataService.delete(this.currentParcel.id)
        .then(response => {
          this.$router.push({ name: "parcels-list" });
        })
        .catch(e => {
          console.log(e);
        });
    }
  },
  mounted() {
    this.message = '';
    this.getAddresses();
    this.getParcel(this.$route.params.id);
  }
};
</script>
<style>
.edit-form {
  max-width: 300px;
  margin: auto;
}
</style>