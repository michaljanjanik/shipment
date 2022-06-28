<template>
  <br>
  <div class="submit-form">
    <div v-if="!submitted">
    <h4>New Parcel</h4>
    <table>
    <tr><td>
        <label for="title"> Number </label>
    </td><td>
        <input
          type="text"
          class="form-control"
          id="title"
          required
          v-model="Parcel.number"
          name="title"
        />
    </td></tr>
    <tr><td>
        <label for="sender_address"> Sender address </label>
    </td><td>

        <select v-model="Parcel.sender_address">
          <option v-for="address in this.addresses" :key="address.id" :value=address.id>
              {{address.name}} {{address.last_name}}  {{address.street }}  {{address.city }}  {{address.post_code }}  {{address.country }}
          </option>
        </select>
    </td></tr>
    <tr><td>
        <label for="sender_address"> Delivery address </label>
    </td><td>
        <select v-model="Parcel.delivery_address">
          <option v-for="address in this.addresses" :key="address.id" :value=address.id>
              {{address.name}} {{address.last_name}}  {{address.street }}  {{address.city }}  {{address.post_code }}  {{address.country }}
          </option>
        </select>
    </td></tr>
    </table>
    <button @click="saveParcel" class="btn btn-success">Submit</button>
    </div>
    <div v-else>
      <h4>You submitted successfully!</h4>
      <button class="btn btn-success" @click="newParcel">Add</button>
    </div>
  </div>
</template>
<script>
import ParcelDataService from '../services/ParcelDataService';
import AddressDataService from '../services/AddressDataService';


export default {
  name: "add-parcel",
  data() {
    return {
      addresses:null,
      Parcel: {
        id: null,
        number: "",
        delivery_address: null,
        sender_address: null,
      },
      submitted: false
    };
  },
  methods: {
    saveParcel() {
      var data = {
        number: this.Parcel.number,
        delivery_address: this.Parcel.delivery_address,
        sender_address: this.Parcel.sender_address
      };
      ParcelDataService.create(data)
        .then(response => {
          this.Parcel.id = response.data.id;
          console.log(response.data);
          this.submitted = true;
        })
        .catch(e => {
          console.log(e);
        });
    },
    newParcel() {
      this.submitted = false;
      this.Parcel = {};
    },
    getAddresses() {
      AddressDataService.getAll()
        .then(response => {
          this.addresses = response.data;
        })
        .catch(e => {
          console.log(e);
        });
    }
  },
  mounted() {
    this.message = '';
    this.getAddresses();
  }

};


</script>
<style>
.submit-form {
  max-width: 300px;
  margin: auto;
}
</style>