import 'dart:convert';

import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter_application_wealth42/Models/therapists.dart';

import 'package:http/http.dart' as http;

class DataProvider with ChangeNotifier {
  String idToken, jwt_token, email, password;
  List<Therapist> therapists = [];

  Future refreshidToken() async {
    print('refresh id token called');
    Map<String, dynamic> body = {
      "email": email,
      "password": password,
      "returnSecureToken": true
    };

    if (email == null && password == null) {
      return;
    }

    var encodedBody = json.encode(body);
    var response = await http.post(
        Uri.parse(
            'https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=AIzaSyBbLVkCU23d9lcWJ9um6sB6QpqQbCAXbGM'),
        body: encodedBody);

    if (response.statusCode == 200) {
      idToken = json.decode(response.body)['idToken'];
    }
    notifyListeners();
    return idToken;
  }

  Future refreshJwt_token() async {
    print('refersh jwt token called');
    Map<String, String> body = {'firebase_id_token': idToken};
    var encodedBody = json.encode(body);
    var response = await http.post(
        Uri.parse('https://b1.wealth42.com/nick-fury/api/firebase-view'),
        body: encodedBody);

    if (json.decode(response.body)['message'] != null) {
      String _idToken = await refreshidToken();
      if (_idToken != null) {
        refreshJwt_token();
      } else {
        return;
      }
    } else {
      jwt_token = json.decode(response.body)['data']['jwt_token'];
    }
    notifyListeners();
    return jwt_token;
  }

  getTherapists() async {
    print('get therapists called');
    var response = await http.get(
        Uri.parse('https://b1.wealth42.com/nick-fury/api/therapist-view'),
        headers: {'Authorization': jwt_token});

    if (therapists.length == 0) {
      if (response.statusCode == 200) {
        if (json.decode(response.body)['message'] != null) {
          await refreshJwt_token();
          getTherapists();
        }
        for (var data in json.decode(response.body)['data']) {
          therapists.add(Therapist.fromJson(data));
        }
      }
    }
    notifyListeners();
  }
}
