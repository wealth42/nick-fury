class Data {
  Data(
    this.x,
    this.y,
  );

  dynamic x;
  double y;

  factory Data.fromJson(Map<String, dynamic> json) => Data(
        json["x"],
        json["y"].toDouble(),
      );

  Map<String, dynamic> toJson() => {
        "x": x,
        "y": y,
      };
}
