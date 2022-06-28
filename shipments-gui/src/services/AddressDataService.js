import http from "../http-commons";

export default class AddressDataService {
  static getAll() {
    return http.get("/address/")
  }
  static  get(id) {
    return http.get(`/address/${id}/`);
  }
  static  create(data) {
    return http.post("/address/", data);
  }
  static  update(id, data) {
    return http.put(`/address/${id}/`, data);
  }
  static  delete(id) {
    return http.delete(`/address/${id}/`);
  }
}

