import 'package:financial_plan/models/chart_details.dart';
import 'package:financial_plan/models/data.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:syncfusion_flutter_charts/charts.dart';

class InvestmentAndLoan extends StatelessWidget {
  const InvestmentAndLoan(
      {this.enableAnimation = true, required this.chartDetails, Key? key})
      : super(key: key);

  final bool enableAnimation;

  final ChartDetails chartDetails;

  @override
  Widget build(BuildContext context) {
    return Container(
      child: SfCartesianChart(
        primaryXAxis: CategoryAxis(
            isVisible: enableAnimation,
            majorGridLines: MajorGridLines(width: 0),
            labelPlacement: LabelPlacement.onTicks),
        primaryYAxis: NumericAxis(
            isVisible: enableAnimation,
            axisLine: AxisLine(width: 0),
            interval: 10000000,
            maximum: 70000000),
        legend: Legend(
            isVisible: enableAnimation,
            overflowMode: LegendItemOverflowMode.wrap),
        title: enableAnimation ? ChartTitle(text: chartDetails.title) : null,
        // onDataLabelRender: (args) {
        //   if (!args.text.contains('%')) args.text += '%';
        // },
        series: [
          SplineSeries<Data, String>(
              name: 'Investment',
              markerSettings: MarkerSettings(isVisible: enableAnimation),
              animationDuration: enableAnimation ? 1000 : 0,
              dataSource: chartDetails.data,
              xValueMapper: (Data data, int i) => data.x!,
              yValueMapper: (Data data, int i) => data.y),
          SplineSeries<Data, String>(
              markerSettings: MarkerSettings(isVisible: enableAnimation),
              name: 'Loan',
              animationDuration: enableAnimation ? 1000 : 0,
              dataSource: chartDetails.data2!,
              xValueMapper: (Data data, int i) => data.x!,
              yValueMapper: (Data data, int i) => data.y)
        ],
      ),
    );
  }
}
