import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:flutter_application_wealth42/DataProvider/dataProvider.dart';
import 'package:flutter_application_wealth42/Models/therapists.dart';
import 'package:flutter_application_wealth42/Screens/searchPage.dart';
import 'package:flutter_application_wealth42/Screens/therapists.dart';
import 'package:flutter_application_wealth42/SignUp/signUp.dart';
import 'package:flutter_application_wealth42/Utils/utils.dart';
import 'package:http/http.dart' as http;
import 'package:provider/provider.dart';

class HomePage extends StatefulWidget {
  String jwt_token;
  HomePage({Key key, this.jwt_token}) : super(key: key);

  @override
  _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  String jwt_token, idToken;
  int active = 0;
  List<Therapist> therapists = [];

  @override
  void initState() {
    super.initState();
    jwt_token = widget.jwt_token;
    // getTherapists();
  }

  Future getHomeView() async {
    var response = await http.get(
        Uri.parse('https://b1.wealth42.com/nick-fury/api/home-view'),
        headers: {'Authorization': jwt_token});
    if (json.decode(response.body)['message'] != null) {
      jwt_token = await Provider.of<DataProvider>(context, listen: false)
          .refreshJwt_token();
      if (jwt_token != null) {
        getHomeView();
      } else {
        Navigator.push(
            context, MaterialPageRoute(builder: (context) => SignUp()));
      }
    } else {
      return json.decode(response.body);
    }
  }

  @override
  Widget build(BuildContext context) {
    jwt_token = Provider.of<DataProvider>(context, listen: true).jwt_token;
    idToken = Provider.of<DataProvider>(context, listen: true).idToken;
    therapists = Provider.of<DataProvider>(context, listen: true).therapists;

    return FutureBuilder(
        future: getHomeView(),
        builder: (context, snapshot) {
          if (snapshot.hasData) {
            return Scaffold(
              backgroundColor: Utils().primaryColor,
              appBar: AppBar(
                toolbarHeight: 100,
                automaticallyImplyLeading: false,
                title: Padding(
                  padding: const EdgeInsets.only(top: 16),
                  child: Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    crossAxisAlignment: CrossAxisAlignment.end,
                    children: [
                      Text(
                        active == 0
                            ? 'Hi Bill!'
                            : active == 1
                                ? 'Search'
                                : 'Chat',
                        style:
                            TextStyle(fontSize: 22, fontWeight: FontWeight.bold),
                      ),
                      active == 0
                          ? IconButton(
                              icon: Icon(
                                Icons.add,
                                color: Utils().buttonColor,
                                size: 40,
                              ),
                              onPressed: () {})
                          : Container()
                    ],
                  ),
                ),
                backgroundColor: Utils().secondaryColor,
              ),
              body: active == 0
                  ? SearchPage()
                  : active == 1
                      ? Therapists()
                      : Container(),
              bottomNavigationBar: buildBottomNavigationBar(),
            );
          } else {
            return Material(
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [CircularProgressIndicator(), Text('Please Wait')],
              ),
            );
          }
        });
  }

  Widget buildBottomNavigationBar() {
    return Container(
      height: 80,
      decoration: BoxDecoration(
        color: Utils().secondaryColor,
        // borderRadius: BorderRadius.only(
        //     topLeft: Radius.circular(16), topRight: Radius.circular(16))
      ),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceEvenly,
        crossAxisAlignment: CrossAxisAlignment.center,
        children: [
          TextButton(
              onPressed: () {
                active = 0;
                setState(() {});
              },
              child: Container(
                height: 30,
                child: active == 0
                    ? Image.asset('assets/images/HomeActive.png')
                    : Image.asset('assets/images/Home.png'),
              )),
          TextButton(
              onPressed: () {
                active = 1;
                setState(() {});
              },
              child: Container(
                height: 30,
                child: active == 1
                    ? Image.asset('assets/images/SearchActive.png')
                    : Image.asset('assets/images/Search.png'),
              )),
          TextButton(
              onPressed: () {
                active = 2;
                setState(() {});
              },
              child: Container(
                height: 30,
                child: active == 2
                    ? Image.asset('assets/images/ChatActive.png')
                    : Image.asset('assets/images/Chat.png'),
              )),
        ],
      ),
    );
  }
}
