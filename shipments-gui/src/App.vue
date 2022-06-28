<template>
<div id="app">
    <nav class="navbar navbar-expand navbar-dark bg-dark">
      <div class="navbar-nav mr-auto">
        <li class="nav-item">
          <router-link to="/parcels" class="nav-link">Parcels</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/addresses" class="nav-link">Address</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/deliveries" class="nav-link">Delivery</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/couriers" class="nav-link">Couriers</router-link>
        </li>
      </div>
    </nav>
    <div class="container mt-6">
      <router-view />
    </div>
  </div>
</template>

<script>


export default {
  name: 'App',
  components: {
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
