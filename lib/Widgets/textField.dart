import 'package:flutter/material.dart';

class CustomTextField extends StatelessWidget {
  final Function onChange;
  final String labelText;
  final bool obscureText;
  final Color color;
  final Icon icon;
  const CustomTextField(
      {Key key,
      @required this.labelText,
      @required this.onChange,
      @required this.obscureText,
      this.color,
      this.icon})
      : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.symmetric(horizontal: 16),
      child: TextFormField(
        onChanged: onChange,
        obscureText: obscureText,
        decoration: InputDecoration(
            fillColor: color == null ? Colors.white : color,
            filled: true,
            prefixIcon: icon,
            floatingLabelBehavior: FloatingLabelBehavior.never,
            border: OutlineInputBorder(
              borderRadius: BorderRadius.circular(10),
              borderSide: BorderSide(color: Colors.transparent),
            ),
            focusedBorder: OutlineInputBorder(
              borderRadius: BorderRadius.circular(10),
              borderSide: BorderSide(
                color: Colors.transparent,
              ),
            ),
            enabledBorder: OutlineInputBorder(
              borderRadius: BorderRadius.circular(10.0),
              borderSide: BorderSide(
                color: Colors.transparent,
              ),
            ),
            labelText: labelText),
      ),
    );
  }
}
