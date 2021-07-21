import 'dart:math';

class Therapist {
  String name, about, stream, therapist_token;
  int experience;
  List specialized_in;

  Therapist(
      {this.name,
      this.about,
      this.stream,
      this.therapist_token,
      this.experience,
      this.specialized_in});

  Therapist.fromJson(Map<String, dynamic> json) {
    name = json['name'];
    about = json['about'];
    stream = json['stream'];
    therapist_token = json['therapist_token'];
    experience = json['experience'];
    specialized_in = json['specialized_in'] ;
  }
}
