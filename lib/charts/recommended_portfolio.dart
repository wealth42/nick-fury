import 'package:financial_plan/models/chart_details.dart';
import 'package:financial_plan/models/data.dart';
import 'package:flutter/material.dart';
// import 'package:syncfusion_flutter_charts/charts.dart';
import 'package:charts_flutter/flutter.dart';

class RecommendedPortfolio extends StatelessWidget {
  const RecommendedPortfolio(
      {this.isFullView = true, required this.chartDetails, Key? key})
      : super(key: key);

  final bool isFullView;

  final ChartDetails chartDetails;

  List<Color> get pallete => <Color>[
        Color.fromHex(code: '#003f5c'),
        Color.fromHex(code: '#2f4b7c'),
        Color.fromHex(code: '#665191'),
        Color.fromHex(code: '#a05195'),
        Color.fromHex(code: '#d45087'),
        Color.fromHex(code: '#f95d6a'),
        Color.fromHex(code: '#ff7c43'),
        Color.fromHex(code: '#ffa600')
      ];

  @override
  Widget build(BuildContext context) {
    final Size size = MediaQuery.of(context).size;
    return Container(
        // child: SfCircularChart(
        //   legend: Legend(
        //       isVisible: isFullView,
        //       overflowMode: LegendItemOverflowMode.wrap),
        //   title: isFullView ? ChartTitle(text: 'chartDetails.title') : null,
        //   onDataLabelRender: (args) {
        //     if (!args.text.contains('%')) args.text += '%';
        //   },
        //   series: [
        //     PieSeries<Data, String>(
        //         strokeWidth: isFullView ? 2 : 0,
        //         dataLabelSettings: DataLabelSettings(
        //             isVisible: isFullView,
        //             labelPosition: ChartDataLabelPosition.outside,
        //             labelIntersectAc78otion: LabelIntersectAction.none),
        //         strokeColor: Colors.white,
        //         enableSmartLabels: true,
        //         animationDuration: isFullView ? 1000 : 0,
        //         dataSource: chartDetails.data,
        //         xValueMapper: (Data data, int i) => data.x!,
        //         yValueMapper: (Data data, int i) => data.y)
        //   ],
        // ),
        child: PieChart<Object>(
      [
        Series<Data, String>(
          id: '0',
          colorFn: (Data _, int? i) => pallete[i!],
          data: chartDetails.data,
          domainFn: (Data data, _) => data.x,
          measureFn: (Data data, _) => data.y,
          outsideLabelStyleAccessorFn: (_, int? i) =>
              TextStyleSpec(color: pallete[i!]),
          labelAccessorFn: (Data data, _) => data.y.toString() + '%',
        )
      ],
      defaultRenderer: ArcRendererConfig<Object>(
          arcRatio: 0.6,
          arcRendererDecorators: isFullView
              ? [
                  ArcLabelDecorator<Object>(
                    outsideLabelStyleSpec:
                        TextStyleSpec(color: Color.black, fontSize: 5),
                    showLeaderLines: false,
                    labelPosition: ArcLabelPosition.outside,
                  )
                ]
              : []),
      behaviors: isFullView
          ? [
              DatumLegend(
                  cellPadding: EdgeInsets.all(2),
                  position: size.shortestSide == size.height
                      ? BehaviorPosition.end
                      : BehaviorPosition.inside,
                  desiredMaxColumns: size.shortestSide == size.height ? 1 : 2,
                  desiredMaxRows: size.shortestSide == size.height ? 10 : 5,
                  horizontalFirst: false,
                  insideJustification: InsideJustification.topStart)
            ]
          : [],
      defaultInteractions: true,
      layoutConfig: isFullView
          ? LayoutConfig(
              leftMarginSpec: MarginSpec.fixedPixel(50),
              topMarginSpec: MarginSpec.fixedPixel(50),
              rightMarginSpec: MarginSpec.fixedPixel(50),
              bottomMarginSpec: MarginSpec.fromPercent(maxPercent: 5))
          : null,
    ));
  }
}
