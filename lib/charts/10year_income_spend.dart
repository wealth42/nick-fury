import 'package:financial_plan/models/chart_details.dart';
import 'package:financial_plan/models/data.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:intl/intl.dart';
import 'package:syncfusion_flutter_charts/charts.dart';

class IncomeAndSpend extends StatelessWidget {
  const IncomeAndSpend(
      {this.isFullView = true, required this.chartDetails, Key? key})
      : super(key: key);

  final bool isFullView;

  final ChartDetails chartDetails;

  @override
  Widget build(BuildContext context) {
    return Container(
      child: SfCartesianChart(
        // plotAreaBorderColor: Colors.transparent,
        primaryXAxis: CategoryAxis(
            isVisible: isFullView,
            labelPlacement: LabelPlacement.onTicks,
            majorGridLines: MajorGridLines(width: 0)),
        primaryYAxis: NumericAxis(
            isVisible: isFullView,
            title: AxisTitle(text: 'Amount in INR'),
            axisLine: AxisLine(width: 0),
            maximum: 40000000,
            interval: 5000000,
            numberFormat: NumberFormat.currency(symbol: '₹', decimalDigits: 0)),
        legend: Legend(
            isVisible: isFullView, overflowMode: LegendItemOverflowMode.wrap),
        title: isFullView ? ChartTitle(text: chartDetails.title) : null,
        // onDataLabelRender: (args) {
        //   if (!args.text.contains('%')) args.text += '%';
        // },
        series: [
          LineSeries<Data, String>(
              name: 'inflow',
              markerSettings: MarkerSettings(isVisible: isFullView),
              animationDuration: isFullView ? 1000 : 0,
              dataSource: chartDetails.data,
              xValueMapper: (Data data, int i) => data.x!,
              yValueMapper: (Data data, int i) => data.y),
          SplineSeries<Data, String>(
              name: 'outflow',
              splineType: SplineType.clamped,
              // cardinalSplineTension: 0,
              markerSettings: MarkerSettings(isVisible: isFullView),
              animationDuration: isFullView ? 1000 : 0,
              dataSource: chartDetails.data2!,
              xValueMapper: (Data data, int i) => data.x!,
              yValueMapper: (Data data, int i) => data.y)
        ],
      ),
    );
  }
}
