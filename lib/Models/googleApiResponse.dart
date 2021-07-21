class GoogleAPIResponse {
  String kind, idToken, email, refreshToken, expiresIn, localId;

  GoogleAPIResponse(
      {this.kind,
      this.idToken,
      this.email,
      this.refreshToken,
      this.expiresIn,
      this.localId});

  GoogleAPIResponse.fromJson(Map<String, dynamic> json) {
    kind = json['kind'];
    idToken = json['idToken'];
    email = json['email'];
    refreshToken = json['refreshToken'];
    expiresIn = json['expiresIn'];
    localId = json['localId'];
  }
}
