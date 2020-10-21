import React, { Component } from "react";
import { connect } from "react-redux";
import { saveLoginDetails } from "../../actions/action";
import { SafeAreaView, Text, TouchableOpacity, View } from "react-native";
import {
  heightPercentageToDP as hp,
  widthPercentageToDP as wp,
} from "react-native-responsive-screen";
import ValidationComponent from "react-native-form-validator";

import { AppButton, AppTextInput } from "../../components";
import styles from "../../config/styles";
import colors from "../../config/colors";

class PatientLogin extends ValidationComponent {
  constructor(props) {
    super(props);
    this.state = {
      username: "",
      password: "",
    };
  }

  async validateState() {
    this.validateForm();
    await this.validateOK();
  }

  validateOK() {
    let { username, password } = this.state;
    if (!this.isFieldInError("username") && !this.isFieldInError("password")) {
      this.props.saveLoginDetails("patient", username, password);
      this.props.navigation.goBack();
      this.props.navigation.navigate("Patient");
    }
  }

  validateForm() {
    this.validate({
      username: { minlength: 4, maxlength: 15, required: true },
      password: { minlength: 4, required: true },
    });
  }

  render() {
    let { username, password } = this.state;
    return (
      <SafeAreaView style={styles.authContainer}>
        <AppTextInput
          placeholder="Username"
          icon="email-outline"
          iconcolor="#000"
          size={20}
          fontSize={18}
          value={username}
          onChangeText={(username) => this.setState({ username })}
        />

        <AppTextInput
          placeholder="Password"
          icon="key-outline"
          size={20}
          fontSize={18}
          secureTextEntry={true}
          value={password}
          onChangeText={(password) => this.setState({ password })}
        />

        {this.isFieldInError("error") &&
          this.getErrorsInField("error").map((errorMessage) => (
            <Text>{errorMessage}</Text>
          ))}
        <View style={styles.buttons}>
          <AppButton
            borderRadius={wp("100")}
            text="Login"
            txtstyle={styles.buttonText}
            style={{ marginBottom: hp("2") }}
            onPress={() => this.validateState()}
          />
          <AppButton
            borderRadius={wp("100")}
            text="Signup"
            txtstyle={styles.buttonText}
            onPress={() => this.props.navigation.navigate("PatientSignup")}
          />
        </View>
        <TouchableOpacity
          onPress={() => console.log("Forgot Password Pressed")}
        >
          <Text style={styles.forgotPassword}>Forgot Password?</Text>
        </TouchableOpacity>
        <Text style={styles.errorText}>{this.getErrorMessages()}</Text>
      </SafeAreaView>
    );
  }
}

const mapStateToProps = (state) => {
  return {
    ...state,
  };
};

export default connect(mapStateToProps, { saveLoginDetails })(PatientLogin);
