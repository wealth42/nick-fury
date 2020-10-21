import React, { Component } from "react";
import { connect } from "react-redux";
import { Text, View, SafeAreaView, TouchableOpacity } from "react-native";
import {
  widthPercentageToDP as wp,
  heightPercentageToDP as hp,
} from "react-native-responsive-screen";
import { MaterialCommunityIcons } from "@expo/vector-icons";

import { AppButton, AppTextInput } from "../../components";
import styles from "../../config/styles";

class PatientHome extends Component {
  constructor(props) {
    super(props);
    this.state = {};
  }

  render() {
    return (
      <SafeAreaView style={styles.homeContainer}>
        <View style={styles.homeTopbar}>
          <AppTextInput
            placeholder="Search Therapists"
            icon="magnify"
            size={hp(2.5)}
            fontSize={15}
            style={{
              width: wp(80),
              marginHorizontal: wp(3),
              backgroundColor: "#fcfcfc",
            }}
          />
          <TouchableOpacity>
            <MaterialCommunityIcons
              name="email-outline"
              size={35}
              color="#fff"
            />
          </TouchableOpacity>
        </View>
        <View style={styles.homeWelcomePlacement}>
          <Text style={styles.title}>
            Welcome {this.props.common.username} !
          </Text>
          <Text style={styles.title}>
            Feelings aren't meant to be bottled up. Tell us how you feel.
          </Text>
          <AppButton
            text="Go to Journal"
            onPress={() => this.props.navigation.navigate("Journal")}
            borderRadius={wp(100)}
          />
        </View>
      </SafeAreaView>
    );
  }
}

const mapStateToProps = (state) => {
  return {
    ...state,
  };
};

export default connect(mapStateToProps, {})(PatientHome);
