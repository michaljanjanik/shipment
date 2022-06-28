<template>
  <br>
    <h4>New Address</h4>
  <div class="submit-form">
    <div v-if="!submitted">
        <table><tr><td>
        <label for="title">Name</label>
        </td><td>
        <input
          type="text"
          class="form-control"
          id="name"
          required
          v-model="Address.name"
          name="name"
        /></td></tr>
        <tr><td>
        <label for="title">Last name</label>
        </td><td>
        <input
          type="text"
          class="form-control"
          id="last_name"
          required
          v-model="Address.last_name"
          name="last_name"
        />
        </td></tr>
        <tr><td>
        <label for="street">Street</label>
        </td><td>
        <input
          type="text"
          class="form-control"
          id="street"
          required
          v-model="Address.street"
          name="street"
        />
        </td></tr>
        <tr><td>
        <label for="city">City</label>
        </td><td>
        <input
          type="text"
          class="form-control"
          id="city"
          required
          v-model="Address.city"
          name="city"
        />
        </td></tr>
        <tr><td>
        <label for="post_code">Post code</label>
        </td><td>
        <input
          type="text"
          class="form-control"
          id="post_code"
          required
          v-model="Address.post_code"
          name="post_code"
        />
        </td></tr>
        <tr><td>
        <label for="country">Country</label>
        </td><td>
        <input
          type="text"
          class="form-control"
          id="country"
          required
          v-model="Address.country"
          name="country"
        />
        </td></tr>
     </table>
    <button @click="saveAddress" class="btn btn-success">Submit</button>
    </div>
    <div v-else>
      <h4>You submitted successfully!</h4>
      <button class="btn btn-success" @click="newAddress">Add</button>
    </div>
  </div>
</template>
<script>
import AddressDataService from '../services/AddressDataService';


export default {
  name: "add-address",
  data() {
    return {
      addresses:null,
      Address: {
        id: null,
        name: "",
        last_name: "",
        street: "",
        city: "",
        post_code: "",
        country: "",
      },
      submitted: false
    };
  },
  methods: {
    saveAddress() {
      var data = {
        name: this.Address.name,
        family_name: this.Address.last_name,
        street: this.Address.street,
        city: this.Address.city,
        post_code: this.Address.post_code,
        country: this.Address.country,
      };

      AddressDataService.create(data)
        .then(response => {
          this.Address.id = response.data.id;
          console.log(response.data);
          this.submitted = true;
        })
        .catch(e => {
          console.log(e);
        });
    },
    newAddress() {
      this.submitted = false;
      this.Address = {};
    },
  },
  mounted() {
  }

};


</script>
<style>
.submit-form {
  max-width: 300px;
  margin: auto;
}
</style>