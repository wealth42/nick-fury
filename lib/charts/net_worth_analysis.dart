import 'package:financial_plan/models/chart_details.dart';
import 'package:financial_plan/models/data.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:intl/intl.dart';
import 'package:syncfusion_flutter_charts/charts.dart';

class NetWorthAnalysis extends StatelessWidget {
  const NetWorthAnalysis(
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
            labelRotation: 90,
            isVisible: isFullView,
            labelPlacement: LabelPlacement.onTicks,
            majorGridLines: MajorGridLines(width: 0),
            crossesAt: 0),
        primaryYAxis: NumericAxis(
            title: AxisTitle(text: 'Amount in INR'),
            isVisible: isFullView,
            axisLine: AxisLine(width: 0),
            minimum: -15000000),
        legend: Legend(
            isVisible: isFullView, overflowMode: LegendItemOverflowMode.wrap),
        title: isFullView ? ChartTitle(text: chartDetails.title) : null,
        // onDataLabelRender: (args) {
        //   if (!args.text.contains('%')) args.text += '%';
        // },
        series: [
          AreaSeries<Data, String>(
              name: 'Asset Class Balance',
              opacity: 0.8,
              animationDuration: isFullView ? 1000 : 0,
              dataSource: chartDetails.data,
              xValueMapper: (Data data, int i) => data.x!,
              yValueMapper: (Data data, int i) => data.y),
          AreaSeries<Data, String>(
              name: 'Loan Principal',
              opacity: 0.8,
              animationDuration: isFullView ? 1000 : 0,
              dataSource: chartDetails.data2!,
              xValueMapper: (Data data, int i) => data.x!,
              yValueMapper: (Data data, int i) => data.y)
        ],
      ),
    );
  }
}
