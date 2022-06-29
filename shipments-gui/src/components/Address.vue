<template>
  <div v-if="currentAddress" class="edit-form">
    <h4>Address</h4>
    <form>
      <table>
        <tr><td>
        <label for="Name">Name</label>
        </td><td>
        <input type="text" class="form-control" id="name"
          v-model="currentAddress.name"
        />
        </td></tr>
        <tr><td>
        <label for="last_name">Last name</label>
        </td><td>
        <input type="text" class="form-control" id="family_name"
          v-model="currentAddress.family_name"
        />
        </td></tr>
        <tr><td>
        <label for="street">Street</label>
        </td><td>
        <input type="text" class="form-control" id="street"
          v-model="currentAddress.street"
        />
        </td></tr>
        <tr><td>
        <label for="city">City</label>
        </td><td>
        <input type="text" class="form-control" id="city"
          v-model="currentAddress.city"
        />
        </td></tr>
        <tr><td>
        <label for="post_code">Post code</label>
        </td><td>
        <input type="text" class="form-control" id="post_code"
          v-model="currentAddress.post_code"
        />
        </td></tr>
        <tr><td>
        <label for="country">country</label>
        </td><td>
        <input type="text" class="form-control" id="coutry"
          v-model="currentAddress.country"
        />
        </td></tr>
      </table>
    </form>
    <button class="badge badge-danger mr-2"
      @click="deleteAddress">
      Delete
    </button>
    <button type="submit" class="badge badge-success"
      @click="updateAddress"
    >
      Update
    </button>
    <p>{{ message }}</p>
  </div>
  <div v-else>
    <br />
    <p>Please click on a address...</p>
  </div>
</template>
<script>
import AddressDataService from '../services/AddressDataService';

export default {
  name: "address-details",
  data() {
    return {
      currentAddress: null,
    };
  },
  methods: {
    getAddress(id) {
      AddressDataService.get(id)
        .then(response => {
          this.currentAddress = response.data;
        })
        .catch(e => {
          console.log(e);
        });
    },
    updateAddress() {
      AddressDataService.update(this.currentAddress.id, this.currentAddress)
        .then(response => {
          this.message = 'The Parcel was updated successfully!';
        })
        .catch(e => {
          console.log(e);
        });
    },
    deleteAddress() {
      AddressDataService.delete(this.currentAddress.id)
        .then(response => {
          this.$router.push({ name: "address-list" });
        })
        .catch(e => {
          console.log(e);
        });
    }
  },
  mounted() {
    this.message = '';
    this.getAddress(this.$route.params.id);
  }
};
</script>
<style>
.edit-form {
  max-width: 300px;
  margin: auto;
}
</style>