<template>
  <div v-if="currentCourier" class="edit-form">
    <h4>Courier</h4>
    <form>
       <table>
       <tr><td>
        <label for="name">Name</label>
        </td><td>
        <input type="text" class="form-control" id="name"
          v-model="currentCourier.name"
        />
        </td></tr>
        <tr><td>
        <label for="last_name">Last name</label>
        </td><td>
        <input type="text" class="form-control" id="last_name"
          v-model="currentCourier.last_name"
        />
        </td></tr>
       </table>
    </form>
    <button class="badge badge-danger mr-2"
      @click="deleteCourier">
      Delete
    </button>
    <button type="submit" class="badge badge-success"
      @click="updateCourier"
    >
      Update
    </button>
    <p>{{ message }}</p>
  </div>
  <div v-else>
    <br />
    <p>Please click on a Courier...</p>
  </div>
</template>
<script>
import CourierDataService from '../services/CourierDataService';


export default {
  name: "courier-details",
  data() {
    return {
      currentCourier: null,
    };
  },
  methods: {
    getCourier(id) {
      CourierDataService.get(id)
        .then(response => {
          this.currentCourier = response.data;
          console.log(response.data);
        })
        .catch(e => {
          console.log(e);
        });
    },
    updateCourier() {
      CourierDataService.update(this.currentCourier.id, this.currentCourier)
        .then(response => {
          console.log(response.data);
          this.message = 'The Courier was updated successfully!';
        })
        .catch(e => {
          console.log(e);
        });
    },
    deleteCourier() {
      CourierDataService.delete(this.currentCourier.id)
        .then(response => {
          this.$router.push({ name: "couriers-list" }); console.log(response);
        })
        .catch(e => {
          console.log(e);
        });
    }
  },
  mounted() {
    this.message = '';
    this.getCourier(this.$route.params.id);
  }
};
</script>
<style>
.edit-form {
  max-width: 300px;
  margin: auto;
}
</style>