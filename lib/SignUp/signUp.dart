import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:flutter_application_wealth42/DataProvider/dataProvider.dart';
import 'package:flutter_application_wealth42/Models/googleApiResponse.dart';
import 'package:flutter_application_wealth42/Screens/homePage.dart';
import 'package:flutter_application_wealth42/SignUp/enterDetails.dart';
import 'package:flutter_application_wealth42/Widgets/button.dart';
import 'package:flutter_application_wealth42/Widgets/textField.dart';
import 'package:http/http.dart' as http;
import 'package:provider/provider.dart';

class SignUp extends StatefulWidget {
  SignUp({Key key}) : super(key: key);

  @override
  _SignUpState createState() => _SignUpState();
}

class _SignUpState extends State<SignUp> {
  String email;
  String password;

  @override
  Widget build(BuildContext context) {
    return SafeArea(
      child: Scaffold(
        backgroundColor: Colors.black,
        body: ListView(
          // mainAxisAlignment: MainAxisAlignment.start,
          children: [
            SizedBox(
              height: 50,
            ),
            Container(
              height: 250,
              // width: MediaQuery.of(context).size.width + 500,
              // constraints: BoxConstraints(maxWidth: 500),
              decoration: BoxDecoration(
                image: DecorationImage(
                    image: AssetImage('assets/images/Group 7.png'),
                    fit: BoxFit.fill),
              ),
            ),
            SizedBox(
              height: 8,
            ),
            Center(
              child: Text(
                'Welcome to muzo',
                style: TextStyle(
                    fontWeight: FontWeight.bold,
                    fontSize: 24,
                    color: Colors.white),
              ),
            ),
            SizedBox(
              height: 32,
            ),
            CustomTextField(
              onChange: (value) {
                email = value;
              },
              labelText: 'Email ID',
              obscureText: false,
            ),
            SizedBox(
              height: 8,
            ),
            CustomTextField(
              labelText: "Password",
              onChange: (value) {
                password = value;
              },
              obscureText: true,
            ),
            CustomButton(
                onPressed: () async {
                  // try {
                  Map<String, String> response;
                  response = await callGoogleAPISignUp(email, password);
                  String idToken = response['idToken'];
                  if (idToken == null) {
                    String error = response['error'];
                    await showDialog(
                        context: context,
                        builder: (context) => AlertDialog(
                              title: Center(child: Text(error)),
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
                  Provider.of<DataProvider>(context, listen: false).email =
                      email;
                                        Provider.of<DataProvider>(context, listen: false).password =
                      password;
                  Navigator.push(
                      context,
                      MaterialPageRoute(
                          builder: (context) => EnterDetailScreen(
                                idToken: idToken,
                              )));
                  // } catch (e) {
                  //   print(e.toString());
                  // }
                },
                text: 'Sign Up'),
                            CustomButton(
                onPressed: () async {
                  // try {
                  Map<String, String> response;
                  response = await callGoogleAPISignIn(email, password);
                  String idToken = response['idToken'];
                  if (idToken == null) {
                    String error = response['error'];
                    await showDialog(
                        context: context,
                        builder: (context) => AlertDialog(
                              title: Center(child: Text(error)),
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
                  Provider.of<DataProvider>(context, listen: false).email =
                      email;
                                        Provider.of<DataProvider>(context, listen: false).password =
                      password;
                  Navigator.push(
                      context,
                      MaterialPageRoute(
                          builder: (context) => HomePage()));
                  // } catch (e) {
                  //   print(e.toString());
                  // }
                },
                text: 'Sign In')
          ],
        ),
      ),
    );
  }

  Future<Map<String, String>> callGoogleAPISignUp(
      String email, String password) async {
    Map body = {
      'email': email,
      'password': password,
      'returnSecureToken': true
    };
    String idToken;

    var encodedBody = json.encode(body);
    var response = await http.post(
        Uri.parse(
            'https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=AIzaSyBbLVkCU23d9lcWJ9um6sB6QpqQbCAXbGM'),
        headers: {"Content-Type": "application/json"},
        body: encodedBody);

    idToken = GoogleAPIResponse.fromJson(json.decode(response.body)).idToken;
    Provider.of<DataProvider>(context, listen: false).idToken = idToken;
    return {
      'idToken': idToken,
      'error': json.decode(response.body)['error'] == null
          ? null
          : json.decode(response.body)['error']['message']
    };
  }

    Future<Map<String, String>> callGoogleAPISignIn(
      String email, String password) async {
    Map body = {
      'email': email,
      'password': password,
      'returnSecureToken': true
    };
    String idToken;

    var encodedBody = json.encode(body);
    var response = await http.post(
        Uri.parse(
            'https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=AIzaSyBbLVkCU23d9lcWJ9um6sB6QpqQbCAXbGM'),
        headers: {"Content-Type": "application/json"},
        body: encodedBody);

    idToken = GoogleAPIResponse.fromJson(json.decode(response.body)).idToken;
    Provider.of<DataProvider>(context, listen: false).idToken = idToken;
    return {
      'idToken': idToken,
      'error': json.decode(response.body)['error'] == null
          ? null
          : json.decode(response.body)['error']['message']
    };
  }
}
