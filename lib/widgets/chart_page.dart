import 'package:flutter/material.dart';

import '../helper.dart';

class ChartView extends StatefulWidget {
  const ChartView(this.chart, {Key? key}) : super(key: key);

  final Widget chart;
  @override
  _ChartViewState createState() => _ChartViewState();
}

class _ChartViewState extends State<ChartView> {
  @override
  Widget build(BuildContext context) {
    return Theme(
      data: ThemeData(
        brightness: Helper.appBrightness,
        primarySwatch: Colors.grey,
      ),
      child: Scaffold(
        appBar: Helper.getAppBar(refreshCallback: () {
          setState(() {});
        }),
        body: Center(
          child: Padding(
            padding: const EdgeInsets.all(8.0),
            child: Container(child: widget.chart),
          ),
        ),
      ),
    );
  }
}
