import 'data.dart';

class ChartDetails {
  ChartDetails(this.title, this.data, [this.data2]);

  String title;
  List<Data> data;
  List<Data>? data2;

  factory ChartDetails.fromJson(Map<String, dynamic> json) => ChartDetails(
      json["title"],
      List<Data>.from(json["data"].map((x) => Data.fromJson(x))),
      json["data2"] != null
          ? List<Data>.from(json["data2"].map((x) => Data.fromJson(x)))
          : null);

  Map<String, dynamic> toJson() => {
        "title": title,
        "data": List<dynamic>.from(data.map((x) => x.toJson())),
      };
}
