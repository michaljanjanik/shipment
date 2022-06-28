import http from "../http-commons";

export default class ParcelDataService {
  static getAll() {
    return http.get("/parcel/")
  }
  static  get(id) {
    return http.get(`/parcel/${id}/`);
  }
  static  create(data) {
    return http.post("/parcel/", data);
  }
  static  update(id, data) {
    return http.put(`/parcel/${id}/`, data);
  }
  static  delete(id) {
    return http.delete(`/parcel/${id}/`);
  }
  static  deleteAll() {
    return http.delete(`/parcel/`);
  }
}

