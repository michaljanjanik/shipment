import { createWebHistory, createRouter } from "vue-router";
const routes =  [
  {
    path: "/parcels",
    alias: "/parcels",
    name: "parcels-list",
    component: () => import("./components/ParcelsList")
  },
  {
    path: "/parcel/:id",
    name: "parcel-details",
    component: () => import("./components/Parcel")
  },
  {
    path: "/addparcel",
    name: "add-parcel",
    component: () => import("./components/AddParcel")
  },
  {
    path: "/addresses",
    alias: "/addresses",
    name: "address-list",
    component: () => import("./components/AddressList")
  },
  {
    path: "/address/:id",
    name: "address-details",
    component: () => import("./components/Address")
  },
  {
    path: "/addaddress",
    name: "add-address",
    component: () => import("./components/AddAddress")
  },
  {
    path: "/couriers",
    alias: "/couriers",
    name: "couriers-list",
    component: () => import("./components/CourierList")
  },
  {
    path: "/courier/:id",
    name: "courier-details",
    component: () => import("./components/Courier")
  },
  {
    path: "/addcourier",
    name: "add-courier",
    component: () => import("./components/AddCourier")
  },
  {
    path: "/deliveries",
    alias: "/deliveries",
    name: "deliveries-list",
    component: () => import("./components/DeliveryList")
  },
  {
    path: "/delivery/:id",
    name: "delivery-details",
    component: () => import("./components/Delivery")
  },
  {
    path: "/adddelivery",
    name: "add-delivery",
    component: () => import("./components/AddDelivery")
  },

];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;