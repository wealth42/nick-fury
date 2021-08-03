import 'package:financial_plan/widgets/chart_tile.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../helper.dart';

class HomeScreen extends StatefulWidget {
  HomeScreen({required this.refreshCallback, Key? key}) : super(key: key);

  final Function refreshCallback;

  @override
  _HomeScreenState createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  late List<ChartTile> chartTiles;

  void getChartTiles(details) {
    chartTiles = <ChartTile>[];
    details.forEach((key, value) {
      chartTiles.add(ChartTile(chartKey: key));
    });
  }

  @override
  void initState() {
    final details = Provider.of<Object>(context, listen: false);
    getChartTiles(details);
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: Helper.getAppBar(refreshCallback: widget.refreshCallback),
      body: Padding(
        padding: const EdgeInsets.all(8.0),
        child: Container(
            child: GridView.count(
          crossAxisCount: 2,
          children: chartTiles,
        )),
      ),
    );
  }
}
