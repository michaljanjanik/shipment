import http from "../http-commons";

export default class CourierDataService {
  static getAll() {
    return http.get("/courier/")
  }
  static  get(id) {
    return http.get(`/courier/${id}/`);
  }
  static  create(data) {
    return http.post("/courier/", data);
  }
  static  update(id, data) {
    return http.put(`/courier/${id}/`, data);
  }
  static  delete(id) {
    return http.delete(`/courier/${id}/`);
  }
}

