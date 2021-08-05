import 'package:financial_plan/models/chart_details.dart';
import 'package:financial_plan/models/data.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:pie_chart/pie_chart.dart';

class CurrentPortfolio extends StatelessWidget {
  const CurrentPortfolio(
      {this.isFullView = true, required this.chartDetails, Key? key})
      : super(key: key);

  final bool isFullView;

  final ChartDetails chartDetails;

  _getDataMap() {
    Map<String, double> map = {};
    chartDetails.data.forEach((element) {
      map[element.x] = element.y;
    });
    return map;
  }

  @override
  Widget build(BuildContext context) {
    ThemeData appTheme = Theme.of(context);
    Map<String, double> dataMap = _getDataMap();

    final dataLabelColor = appTheme.brightness == Brightness.dark
        ? appTheme.accentColor
        : Colors.black;
    return Container(
        // child: SfCircularChart(
        //   legend: Legend(
        //       isVisible: isFullView,
        //       overflowMode: LegendItemOverflowMode.wrap),
        //   title: isFullView ? ChartTitle(text: chartDetails.title) : null,
        //   onDataLabelRender: (args) {
        //     if (!args.text.contains('%')) args.text += '%';
        //   },
        //   series: [
        //     PieSeries<Data, String>(
        //         strokeWidth: isFullView ? 2 : 0,
        //         dataLabelSettings: DataLabelSettings(
        //             isVisible: isFullView,
        //             labelPosition: ChartDataLabelPosition.outside,
        //             labelIntersectAction: LabelIntersectAction.none),
        //         strokeColor: Colors.white,
        //         enableSmartLabels: true,
        //         animationDuration: isFullView ? 1000 : 0,
        //         dataSource: chartDetails.data,
        //         xValueMapper: (Data data, int i) => data.x!,
        //         yValueMapper: (Data data, int i) => data.y)
        //   ],
        // ),
        child: PieChart(
      dataMap: dataMap,
      chartRadius: MediaQuery.of(context).size.shortestSide / 2,
      chartValuesOptions: ChartValuesOptions(
          chartValueStyle: TextStyle(color: dataLabelColor),
          showChartValuesOutside: true,
          showChartValues: isFullView,
          showChartValuesInPercentage: true,
          chartValueBackgroundColor: Theme.of(context).primaryColor),
      chartType: ChartType.disc,
      legendOptions: LegendOptions(
          showLegends: isFullView,
          legendPosition: LegendPosition.bottom,
          showLegendsInRow: true),
    ));
  }
}
