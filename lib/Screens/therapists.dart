import 'package:flutter/material.dart';
import 'package:flutter_application_wealth42/DataProvider/dataProvider.dart';
import 'package:flutter_application_wealth42/Models/therapists.dart';
import 'package:flutter_application_wealth42/Utils/utils.dart';
import 'package:flutter_application_wealth42/Widgets/textField.dart';
import 'package:provider/provider.dart';

class Therapists extends StatefulWidget {
  Therapists({
    Key key,
  }) : super(key: key);

  @override
  _TherapistsState createState() => _TherapistsState();
}

class _TherapistsState extends State<Therapists> {
  List<Therapist> therapists = [];
  List<bool> control = [
    true,
    false,
    false,
    false,
    false,
    false,
    false,
    false,
    false,
    false,
    false,
    false
  ];
  @override
  void initState() {
    super.initState();
    Provider.of<DataProvider>(context, listen: false).getTherapists();
  }

  @override
  Widget build(BuildContext context) {
    therapists = Provider.of<DataProvider>(context, listen: true).therapists;
    return Column(
      children: [
        Padding(
          padding: const EdgeInsets.symmetric(vertical: 16),
          child: Container(
            height: 45,
            child: CustomTextField(
                labelText: 'Search for therapist',
                onChange: (_) {},
                color: Colors.grey,
                icon: Icon(Icons.search),
                obscureText: false),
          ),
        ),
        Expanded(
          child: ListView(
            children: [
              for (int index = 0; index < therapists.length; index++)
                Padding(
                  padding:
                      const EdgeInsets.symmetric(horizontal: 24, vertical: 16),
                  child: Container(
                    height: 150,
                    decoration: BoxDecoration(
                        color: Colors.black,
                        borderRadius: BorderRadius.all(Radius.circular(8))),
                    child: Row(
                      children: [
                        SizedBox(
                          width: 8,
                        ),
                        Expanded(
                          flex: 3,
                          child: Container(
                            decoration: BoxDecoration(
                                shape: BoxShape.circle, color: Colors.grey),
                          ),
                        ),
                        SizedBox(
                          width: 8,
                        ),
                        Expanded(
                            flex: 7,
                            child: Column(
                              mainAxisAlignment: MainAxisAlignment.center,
                              crossAxisAlignment: CrossAxisAlignment.start,
                              children: [
                                Text(
                                  therapists[index].name,
                                  style: TextStyle(
                                      color: Colors.white,
                                      fontSize: 16,
                                      fontWeight: FontWeight.bold),
                                ),
                                SizedBox(
                                  height: 8,
                                ),
                                Text(
                                  'Description Description',
                                  style: TextStyle(color: Colors.white),
                                ),
                                SizedBox(
                                  height: 4,
                                ),
                                Text(
                                  '24th May 2:02PM',
                                  style: TextStyle(color: Colors.white),
                                ),
                                SizedBox(
                                  height: 16,
                                ),
                                Text(
                                  'View Details',
                                  style: TextStyle(color: Colors.grey),
                                )
                              ],
                            )),
                        Expanded(
                          flex: 4,
                          child: Column(
                            mainAxisAlignment: MainAxisAlignment.spaceBetween,
                            children: [
                              SizedBox(
                                height: 8,
                              ),
                              InkWell(
                                onTap: () {
                                  control[index] = !control[index];
                                  setState(() {});
                                },
                                child: Container(
                                  decoration: BoxDecoration(
                                      color: Color(0xFF202020),
                                      shape: BoxShape.circle),
                                  height: 50,
                                  child: Padding(
                                    padding: const EdgeInsets.all(16.0),
                                    child: control[index]
                                        ? Image.asset(
                                            'assets/images/HeartActive.png',
                                            fit: BoxFit.fill,
                                          )
                                        : Image.asset(
                                            'assets/images/HeartUnactive.png',
                                            fit: BoxFit.fill,
                                          ),
                                  ),
                                ),
                              ),
                              TextButton(
                                  onPressed: () {},
                                  child: Container(
                                    decoration: BoxDecoration(
                                        borderRadius: BorderRadius.all(
                                            Radius.circular(64)),
                                        border: Border.all(
                                            color: Utils().buttonColor)),
                                    child: Padding(
                                      padding: const EdgeInsets.symmetric(
                                          horizontal: 16, vertical: 8),
                                      child: Text(
                                        'Book',
                                        style: TextStyle(
                                            color: Utils().buttonColor),
                                      ),
                                    ),
                                  ))
                            ],
                          ),
                        )
                      ],
                    ),
                  ),
                )
            ],
          ),
        ),
      ],
    );
  }
}
