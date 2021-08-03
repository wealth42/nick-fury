import 'package:financial_plan/models/chart_details.dart';

import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../helper.dart';
import 'chart_page.dart';

class ChartTile extends StatelessWidget {
  const ChartTile({required this.chartKey, Key? key}) : super(key: key);

  final String chartKey;

  @override
  Widget build(BuildContext context) {
    final dynamic charts = Provider.of<Object>(context, listen: false);
    Size size = MediaQuery.of(context).size;
    final ChartDetails chartDetails = ChartDetails.fromJson(charts[chartKey]);
    final cardSize =
        size.height > size.width ? size.width / 2 : (size.height / 2 - 180);
    return Padding(
      padding: const EdgeInsets.all(8.0),
      child: Container(
        width: cardSize,
        height: cardSize,
        child: ElevatedButton(
          // style: ButtonStyle(padding: EdgeInsets.zero),
          onPressed: () {
            Navigator.push(context, MaterialPageRoute(builder: (context) {
              return ChartView(Helper.getChart(chartKey, chartDetails, true));
            }));
          },
          child: Container(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.start,
              mainAxisSize: MainAxisSize.min,
              children: [
                Expanded(
                    child: IgnorePointer(
                        ignoring: true,
                        child: Helper.getChart(chartKey, chartDetails, false))),
                Padding(
                  padding: const EdgeInsets.all(8.0),
                  child: Text(
                    chartDetails.title,
                    maxLines: 2,
                    overflow: TextOverflow.ellipsis,
                  ),
                )
              ],
            ),
            alignment: Alignment.bottomCenter,
          ),
        ),
      ),
    );
  }
}
