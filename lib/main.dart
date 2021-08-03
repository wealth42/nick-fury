import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:provider/provider.dart';

import 'helper.dart';
import 'screens/home_screen.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatefulWidget {
  @override
  State<StatefulWidget> createState() {
    return MyAppState();
  }
}

class MyAppState extends State<MyApp> {
  @override
  Widget build(BuildContext context) {
    return FutureBuilder<dynamic>(
      future: loadChartDetails(context),
      builder: (context, snapshot) {
        if (snapshot.hasError) {
          return Center(
            child: Text("An error occured"),
          );
        }
        if (snapshot.data == null ||
            snapshot.connectionState != ConnectionState.done) {
          return Center(
            child: CircularProgressIndicator(),
          );
        }
        return Provider<Object>.value(
          value: snapshot.data,
          builder: (context, child) {
            return MaterialApp(
                title: 'Financial Plan',
                theme: ThemeData(
                    brightness: Helper.appBrightness,
                    primarySwatch: Colors.grey),
                home: SafeArea(
                  child: HomeScreen(refreshCallback: () {
                    setState(() {});
                  }),
                ));
          },
        );
      },
    );
  }

  Future loadChartDetails(context) async {
    final jsonData = await DefaultAssetBundle.of(context)
        .loadString("assets/data_source.json");
    final data = json.decode(jsonData);
    return data;
  }
}
