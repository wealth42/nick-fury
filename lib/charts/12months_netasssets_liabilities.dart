import 'package:financial_plan/models/chart_details.dart';
import 'package:financial_plan/models/data.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:syncfusion_flutter_charts/charts.dart';

class NetAssetsAndLiabilities extends StatelessWidget {
  const NetAssetsAndLiabilities(
      {this.enableAnimation = true, required this.chartDetails, Key? key})
      : super(key: key);

  final bool enableAnimation;

  final ChartDetails chartDetails;

  @override
  Widget build(BuildContext context) {
    return Container(
      child: SfCartesianChart(

        primaryXAxis: CategoryAxis(isVisible: enableAnimation, crossesAt: 0, labelPlacement: LabelPlacement.onTicks, ),
        primaryYAxis: NumericAxis(isVisible: enableAnimation, axisLine: AxisLine(width: 0), title: AxisTitle(text: 'Amount in INR')),
        legend: Legend(
            isVisible: enableAnimation,
            overflowMode: LegendItemOverflowMode.wrap),
        title: enableAnimation ? ChartTitle(text: chartDetails.title) : null,
        // onDataLabelRender: (args) {
        //   if (!args.text.contains('%')) args.text += '%';
        // },
        series: [
          AreaSeries<Data, String>(
            name: 'Asset Class Balance',
            opacity: 0.8,
              animationDuration: enableAnimation ? 1000 : 0,
              dataSource: chartDetails.data,
              xValueMapper: (Data data, int i) => data.x!,
              yValueMapper: (Data data, int i) => data.y),
              AreaSeries<Data, String>(
                name: 'Loan Principal',
                opacity: 0.8,
              animationDuration: enableAnimation ? 1000 : 0,
              dataSource: chartDetails.data2!,
              xValueMapper: (Data data, int i) => data.x!,
              yValueMapper: (Data data, int i) => data.y)
        ],
      ),
    );
  }
}
