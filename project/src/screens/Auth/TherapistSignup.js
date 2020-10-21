import React, { Component } from "react";
import { connect } from "react-redux";

import { SafeAreaView, Text, View } from "react-native";
import {
  heightPercentageToDP as hp,
  widthPercentageToDP as wp,
} from "react-native-responsive-screen";
import ValidationComponent from "react-native-form-validator";

import { AppButton, AppTextInput } from "../../components";
import styles from "../../config/styles";

export class TherapistSignup extends ValidationComponent {
  constructor(props) {
    super(props);
    this.state = {
      username: "",
      password: "",
      passwordConfirm: "",
      medID: "",
    };
  }

  validateForm() {
    this.validate({
      username: { minlength: 4, maxlength: 15, required: true },
      password: { minlength: 4, required: true },
      passwordConfirm: {
        minlength: 4,
        required: true,
        equalPassword: this.state.password,
      },
      medID: { required: true },
    });
  }

  render() {
    let { username, password, medID, passwordConfirm } = this.state;
    return (
      <SafeAreaView style={styles.authContainer}>
        <Text style={styles.title}>Create Your account</Text>
        <AppTextInput
          placeholder="Username"
          icon="email-outline"
          iconcolor="#000"
          size={hp("3")}
          fontSize={18}
          value={username}
          onChangeText={(username) => this.setState({ username })}
        />
        <AppTextInput
          placeholder="Enter your Medical ID"
          icon="id-card"
          iconcolor="#000"
          size={hp("3")}
          fontSize={18}
          value={medID}
          onChangeText={(medID) => this.setState({ medID })}
        />
        <AppTextInput
          placeholder="Password"
          icon="key-outline"
          secureTextEntry={true}
          size={hp("3")}
          fontSize={18}
          value={password}
          onChangeText={(password) => this.setState({ password })}
        />
        <AppTextInput
          placeholder="Re-enter Password"
          icon="key-outline"
          secureTextEntry={true}
          size={hp("3")}
          fontSize={18}
          value={passwordConfirm}
          onChangeText={(passwordConfirm) => this.setState({ passwordConfirm })}
        />

        {this.isFieldInError("error") &&
          this.getErrorsInField("error").map((errorMessage) => (
            <Text>{errorMessage}</Text>
          ))}
        <View style={styles.buttons}>
          <AppButton
            borderRadius={wp("100")}
            text="Create Account"
            txtstyle={styles.buttonText}
            onPress={() => this.validateForm()}
          />
        </View>

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

export default connect(mapStateToProps, {})(TherapistSignup);
