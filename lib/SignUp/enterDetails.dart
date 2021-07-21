import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:flutter_application_wealth42/Models/userViewResponse.dart';
import 'package:flutter_application_wealth42/Screens/homePage.dart';
import 'package:flutter_application_wealth42/Widgets/button.dart';
import 'package:flutter_application_wealth42/Widgets/textField.dart';
import 'package:http/http.dart' as http;

class EnterDetailScreen extends StatefulWidget {
  String idToken;
  EnterDetailScreen({Key key, @required this.idToken}) : super(key: key);

  @override
  _EnterDetailScreenState createState() => _EnterDetailScreenState();
}

class _EnterDetailScreenState extends State<EnterDetailScreen> {
  String firstName, lastName, city, idToken;

  @override
  void initState() {
    super.initState();
    idToken = widget.idToken;
  }

  @override
  Widget build(BuildContext context) {
    return SafeArea(
      child: Scaffold(
        backgroundColor: Colors.black,
        body: ListView(
          children: [
            SizedBox(
              height: 32,
            ),
            Center(
              child: Text(
                'Please confirm the details',
                style: TextStyle(
                    color: Colors.white,
                    fontSize: 16,
                    fontWeight: FontWeight.bold),
              ),
            ),
            CustomTextField(
                labelText: 'First Name',
                onChange: (value) {
                  firstName = value;
                },
                obscureText: false),
            SizedBox(
              height: 8,
            ),
            CustomTextField(
                labelText: 'Last Name',
                onChange: (value) {
                  lastName = value;
                },
                obscureText: false),
            SizedBox(
              height: 8,
            ),
            CustomTextField(
                labelText: 'City',
                onChange: (value) {
                  city = value;
                },
                obscureText: false),
            CustomButton(
                onPressed: () async {
                  try {
                                      Map<String, String> response =
                      await postUserViewAPI(idToken, firstName, lastName, city);
                  String jwt_token = response['jwt_token'];
                  if (jwt_token == null) {
                    String message = response['message'];
                    await showDialog(
                        context: context,
                        builder: (context) => AlertDialog(
                              title: Center(child: Text(message)),
                              actions: [
                                TextButton(
                                    onPressed: () {
                                      Navigator.pop(context);
                                    },
                                    child: Text('OK'))
                              ],
                            ));
                    return;
                  }
                  Navigator.push(context,
                      MaterialPageRoute(builder: (context) => HomePage(jwt_token: jwt_token,)));
                  } catch (e) {
                    print(e.toString());
                  }

                },
                text: 'Next')
          ],
        ),
      ),
    );
  }

  Future<Map<String, String>> postUserViewAPI(
      String idToken, String firstName, String lastName, String city) async {
    Map body = {
      "firebase_id_token": idToken,
      "first_name": firstName,
      "last_name": lastName,
      "city": city
    };

    var encodedBody = json.encode(body);

    var response = await http.post(
        Uri.parse('https://b1.wealth42.com/nick-fury/api/user-view'),
        body: encodedBody);

    String jwt_token =
        UserViewResponse.fromJson(json.decode(response.body)).jwt_token;
    String message =
        UserViewResponse.fromJson(json.decode(response.body)).message;

    return {'jwt_token': jwt_token, 'message': message};
  }

}
