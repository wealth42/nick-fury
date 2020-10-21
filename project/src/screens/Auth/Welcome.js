import React, { Component } from "react";
import { connect } from "react-redux";
import { Image, Text, View } from "react-native";
import {
  heightPercentageToDP as hp,
  widthPercentageToDP as wp,
} from "react-native-responsive-screen";

import { AppButton } from "../../components";
import styles from "../../config/styles";
import colors from "../../config/colors";

class Welcome extends Component {
  constructor(props) {
    super(props);
    this.state = {};
  }

  render() {
    return (
      <View style={styles.authContainer}>
        <Image
          source={require("../../assets/AppLogo.png")}
          style={styles.welcomeImage}
        />
        <Text style={styles.title}>Welcome</Text>
        <Text style={styles.subtitle}>Please select your identity</Text>

        <AppButton
          text="Patient"
          style={{ marginVertical: hp("3") }}
          borderRadius={25}
          txtstyle={{ fontSize: 20, fontFamily: "normal" }}
          onPress={() => this.props.navigation.navigate("PatientLogin")}
        />
        <AppButton
          text="Therapist"
          borderRadius={25}
          style={{ height: hp("7"), width: wp("80") }}
          txtstyle={{ fontSize: 20 }}
          onPress={() => this.props.navigation.navigate("TherapistLogin")}
        />
        <View style={styles.buttons}></View>
      </View>
    );
  }
}

const mapStateToProps = (state) => {
  return {
    ...state,
  };
};

export default connect(mapStateToProps, {})(Welcome);
