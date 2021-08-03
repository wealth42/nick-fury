import 'package:financial_plan/models/chart_details.dart';
import 'package:financial_plan/models/data.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:syncfusion_flutter_charts/charts.dart';

class CurrentPortfolio extends StatelessWidget {
  const CurrentPortfolio(
      {this.enableAnimation = true, required this.chartDetails, Key? key})
      : super(key: key);

  final bool enableAnimation;

  final ChartDetails chartDetails;

  @override
  Widget build(BuildContext context) {
    return Container(
      child: SfCircularChart(
        legend: Legend(
            isVisible: enableAnimation,
            overflowMode: LegendItemOverflowMode.wrap),
        title: enableAnimation ? ChartTitle(text: chartDetails.title) : null,
        onDataLabelRender: (args) {
          if (!args.text.contains('%')) args.text += '%';
        },
        series: [
          PieSeries<Data, String>(
              strokeWidth: enableAnimation ? 2 : 0,
              dataLabelSettings: DataLabelSettings(
                  isVisible: enableAnimation,
                  labelPosition: ChartDataLabelPosition.outside,
                  labelIntersectAction: LabelIntersectAction.none),
              strokeColor: Colors.white,
              enableSmartLabels: true,
              animationDuration: enableAnimation ? 1000 : 0,
              dataSource: chartDetails.data,
              xValueMapper: (Data data, int i) => data.x!,
              yValueMapper: (Data data, int i) => data.y)
        ],
      ),
    );
  }
}
