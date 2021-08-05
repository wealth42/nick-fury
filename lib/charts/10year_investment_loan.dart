import 'package:financial_plan/models/chart_details.dart';
import 'package:financial_plan/models/data.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:syncfusion_flutter_charts/charts.dart';

class InvestmentAndLoan extends StatelessWidget {
  const InvestmentAndLoan(
      {this.isFullView = true, required this.chartDetails, Key? key})
      : super(key: key);

  final bool isFullView;

  final ChartDetails chartDetails;

  @override
  Widget build(BuildContext context) {
    return Container(
      child: SfCartesianChart(
        primaryXAxis: CategoryAxis(
            isVisible: isFullView,
            majorGridLines: MajorGridLines(width: 0),
            labelPlacement: LabelPlacement.onTicks),
        primaryYAxis: NumericAxis(
            isVisible: isFullView,
            axisLine: AxisLine(width: 0),
            interval: 10000000,
            maximum: 70000000),
        legend: Legend(
            isVisible: isFullView, overflowMode: LegendItemOverflowMode.wrap),
        title: isFullView ? ChartTitle(text: chartDetails.title) : null,
        // onDataLabelRender: (args) {
        //   if (!args.text.contains('%')) args.text += '%';
        // },
        series: [
          SplineSeries<Data, String>(
              name: 'Investment',
              markerSettings: MarkerSettings(isVisible: isFullView),
              animationDuration: isFullView ? 1000 : 0,
              dataSource: chartDetails.data,
              xValueMapper: (Data data, int i) => data.x!,
              yValueMapper: (Data data, int i) => data.y),
          SplineSeries<Data, String>(
              markerSettings: MarkerSettings(isVisible: isFullView),
              name: 'Loan',
              animationDuration: isFullView ? 1000 : 0,
              dataSource: chartDetails.data2!,
              xValueMapper: (Data data, int i) => data.x!,
              yValueMapper: (Data data, int i) => data.y)
        ],
      ),
    );
  }
}
