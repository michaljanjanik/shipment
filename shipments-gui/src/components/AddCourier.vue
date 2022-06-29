<template>
  <br>
    <h4>New Courier</h4>
  <div class="submit-form">
    <div v-if="!submitted">
    <table>
    <tr><td>
        <label for="name">Name</label>
    </td><td>
        <input
          type="text"
          class="form-control"
          id="name"
          required
          v-model="Courier.name"
          name="name"
        />
     </td></tr>
    <tr><td>
        <label for="last_name">Last name</label>
    </td><td>
        <input
          type="text"
          class="form-control"
          id="last_name"
          required
          v-model="Courier.last_name"
          name="last_name"
        />
     </td></tr>
    </table>
    <button @click="saveCourier" class="btn btn-success">Submit</button>
    </div>
    <div v-else>
      <h4>You submitted successfully!</h4>
      <button class="btn btn-success" @click="newCourier">Add</button>
    </div>
  </div>
</template>
<script>
import CourierDataService from '../services/CourierDataService';


export default {
  name: "add-courier",
  data() {
    return {
      Courier: {
        id: null,
        name: "",
        last_name: "",
      },
      submitted: false
    };
  },
  methods: {
    saveCourier() {
      var data = {
        name: this.Courier.name,
        last_name: this.Courier.last_name,
      };
      CourierDataService.create(data)
        .then(response => {
          this.Courier.id = response.data.id;
          this.submitted = true;
        })
        .catch(e => {
          console.log(e);
        });
    },
    newCourier() {
      this.submitted = false;
      this.Courier = {};
    },
  },
  mounted() {
    this.message = '';
  }

};


</script>
<style>
.submit-form {
  max-width: 300px;
  margin: auto;
}
</style>