import 'package:flutter/material.dart';
import 'package:flutter_application_wealth42/Widgets/textField.dart';
import 'package:http/http.dart';

class SearchPage extends StatefulWidget {
  SearchPage({Key key}) : super(key: key);

  @override
  _SearchPageState createState() => _SearchPageState();
}

class _SearchPageState extends State<SearchPage> {
  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Padding(
          padding:
              const EdgeInsets.all(16),
          child: Row(
            children: [
              Expanded(
                flex: 9,
                child: Container(
                  height: 45,
                  child: CustomTextField(
                      labelText: 'Search in journal',
                      onChange: (_) {},
                      color: Colors.grey,
                      icon: Icon(Icons.search),
                      obscureText: false),
                ),
              ),
              SizedBox(
                width: 16,
              ),
              Expanded(
                  flex: 1,
                  child: Image.asset('assets/images/Funnel.png'))
            ],
          ),
        ),
        Expanded(
          child: ListView(
            children: [
              for (int i = 0; i < 3; i++)
                Padding(
                  padding: const EdgeInsets.only(
                      top: 0, left: 16, right: 16, bottom: 16),
                  child: Container(
                    height: 270,
                    decoration: BoxDecoration(color: Colors.black),
                    child: Padding(
                      padding: const EdgeInsets.all(10.0),
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Container(
                            color: Color(0xFFC4C4C4),
                            height: 150,
                          ),
                          SizedBox(
                            height: 8,
                          ),
                          Text(
                            'Headline',
                            style: TextStyle(
                                color: Colors.white,
                                fontWeight: FontWeight.bold,
                                fontSize: 16),
                          ),
                          SizedBox(
                            height: 4,
                          ),
                          Text(
                            'Description Description Description',
                            style: TextStyle(color: Colors.white),
                          ),
                          Text(
                            'Description Description Description',
                            style: TextStyle(color: Colors.white),
                          ),
                          SizedBox(
                            height: 16,
                          ),
                          Row(
                            children: [
                              InkWell(
                                onTap: () {},
                                child: Text(
                                  'Feeling',
                                  style: TextStyle(color: Colors.grey),
                                ),
                              ),
                              SizedBox(
                                width: 32,
                              ),
                              InkWell(
                                onTap: () {},
                                child: Text(
                                  'Date',
                                  style: TextStyle(color: Colors.grey),
                                ),
                              )
                            ],
                          )
                        ],
                      ),
                    ),
                  ),
                )
            ],
          ),
        )
      ],
    );
  }
}
