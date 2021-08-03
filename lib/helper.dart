import 'package:financial_plan/charts/net_worth_analysis.dart';
import 'package:flutter/material.dart';

import 'charts/10year_income_spend.dart';
import 'charts/10year_investment_loan.dart';
import 'charts/12months_netasssets_liabilities.dart';
import 'charts/current_portfolio.dart';
import 'charts/recommended_portfolio.dart';
import 'models/chart_details.dart';

class Helper {
  static Brightness appBrightness = Brightness.dark;
  static getAppBar({required Function refreshCallback}) {
    return AppBar(
        titleSpacing: 1,
        actions: [
          Switch(
              value: appBrightness == Brightness.dark,
              onChanged: (value) {
                appBrightness = value ? Brightness.dark : Brightness.light;
                refreshCallback();
              })
        ],
        leading: Image.asset('logo.png'),
        title: Text('Wealth42'));
  }

  static Widget getChart(
      String key, ChartDetails chartDetails, bool enableAnimation) {
    switch (key) {
      case 'current_portfolio':
        return CurrentPortfolio(
          enableAnimation: enableAnimation,
          chartDetails: chartDetails,
        );
      case 'recommended_portfolio':
        return RecommendedPortfolio(
          enableAnimation: enableAnimation,
          chartDetails: chartDetails,
        );
      case '10years_income_&_spends':
        return IncomeAndSpend(
          enableAnimation: enableAnimation,
          chartDetails: chartDetails,
        );
      case '10years_investment_&_loan':
        return InvestmentAndLoan(
          enableAnimation: enableAnimation,
          chartDetails: chartDetails,
        );
      case '12months_netassets_&_liabilities':
        return NetAssetsAndLiabilities(
          enableAnimation: enableAnimation,
          chartDetails: chartDetails,
        );
      case 'net_worth_analysis':
        return NetWorthAnalysis(
          enableAnimation: enableAnimation,
          chartDetails: chartDetails,
        );
      default:
        return Container();
    }
  }
}
