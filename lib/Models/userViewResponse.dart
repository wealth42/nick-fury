class UserViewResponse {
  String status, firebase_id, first_name, last_name, city, jwt_token, message;
  int id;

  UserViewResponse.fromJson(Map<String, dynamic> json) {
    status = json['status'];
    message = json['message'];
    firebase_id = json['data']['firebase_id'];
    id = json['data']['id'];
    first_name = json['data']['first_name'];
    last_name = json['data']['last_name'];
    city = json['data']['city'];
    jwt_token = json['data']['jwt_token'];
  }
}
