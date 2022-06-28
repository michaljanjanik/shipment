import http from "../http-commons";

export default class DeliveryDataService {
  static getAll() {
    return http.get("/delivery/")
  }
  static  get(id) {
    return http.get(`/delivery/${id}/`);
  }
  static  create(data) {
    return http.post("/delivery/", data);
  }
  static  update(id, data) {
    return http.put(`/delivery/${id}/`, data);
  }
  static  delete(id) {
    return http.delete(`/delivery/${id}/`);
  }
  static  deleteAll() {
    return http.delete(`/delivery/`);
  }
}

