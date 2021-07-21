import 'package:flutter/material.dart';
import 'package:flutter_application_wealth42/Utils/utils.dart';

class CustomButton extends StatelessWidget {
  final Function onPressed;
  final String text;
  const CustomButton({Key key, @required this.onPressed, @required this.text}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return TextButton(
        onPressed: onPressed,
        child: Padding(
          padding: EdgeInsets.symmetric(horizontal: 8),
          child: Container(
            width: MediaQuery.of(context).size.width,
            height: 60,
            decoration: BoxDecoration(
                borderRadius: BorderRadius.all(Radius.circular(10)),
                color: Utils().buttonColor),
            child: Center(
              child: Text(
                text,
                style: TextStyle(
                    color: Colors.black,
                    fontSize: 16,
                    fontWeight: FontWeight.bold),
              ),
            ),
          ),
        ));
  }
}
