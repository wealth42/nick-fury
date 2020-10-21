import React, { Component } from "react";
import { connect } from "react-redux";

import {
  FlatList,
  Modal,
  Text,
  View,
  ActivityIndicator,
  TouchableOpacity,
} from "react-native";
import {
  heightPercentageToDP as hp,
  widthPercentageToDP as wp,
} from "react-native-responsive-screen";

import {
  AppButton,
  ListItems,
  ListItemSeparator,
  MyIcon,
} from "../../components";
import styles from "../../config/styles";
import colors from "../../config/colors";

class TherapistList extends Component {
  constructor(props) {
    super(props);
    this.state = {
      modalVisible: false,
      therapistList: [],
      isLoading: true,
      therapistName: "",
    };
  }

  componentDidMount() {
    fetch("https://5f887647a8a2b5001641ec8b.mockapi.io/my-therapists")
      .then((response) => response.json())
      .then((responseJson) => {
        this.setState({ isLoading: false, therapistList: responseJson });
      });
  }

  render() {
    return (
      <View style={styles.screenBackground}>
        {this.state.isLoading && (
          <View
            style={{
              elevation: 1000,
              position: "absolute",
              paddingHorizontal: wp(50),
              paddingVertical: hp(50),
            }}
          >
            <ActivityIndicator color={colors.primaryVioletDark} size="large" />
          </View>
        )}

        <View style={styles.bannerContainer}>
          <View style={styles.banner}>
            <Text style={styles.bannerTitle}>Your Therapists</Text>
          </View>
        </View>
        <View style={styles.seperator} />
        <FlatList
          data={this.state.therapistList}
          keyExtractor={(item) => item.id}
          renderItem={({ item }) => (
            <View>
              <TouchableOpacity
                onPress={() =>
                  this.setState({
                    modalVisible: true,
                    therapistName: item.name,
                  })
                }
              >
                <ListItems image={item.avatar} title={item.name} size={100} />
              </TouchableOpacity>
            </View>
          )}
          ItemSeparatorComponent={ListItemSeparator}
        />

        <Modal
          visible={this.state.modalVisible}
          onRequestClose={() => this.setState({ modalVisible: false })}
          animationType={"slide"}
        >
          <View style={styles.screenBackground}>
            <View style={styles.bannerContainer}>
              <View style={styles.banner}>
                <Text style={styles.bannerTitle}>
                  {this.state.therapistName}
                </Text>
              </View>
            </View>
            <View style={styles.bannerContainer}>
              <AppButton
                borderRadius={25}
                text="Close"
                txtstyle={{ fontSize: 20 }}
                onPress={() => this.setState({ modalVisible: false })}
                style={{ marginVertical: hp(5) }}
              />
            </View>

            <View style={styles.listBackground}>
              <TouchableOpacity
                onPress={() => console.log("Message Therapist PRESSED")}
              >
                <ListItems
                  IconComponent={
                    <MyIcon
                      name="message-bulleted"
                      backgroundColor="#836fa9"
                      IconSize={50}
                    />
                  }
                  title="Message Therapist"
                  size={hp(15)}
                />
              </TouchableOpacity>
            </View>
            <View style={styles.listBackground}>
              <TouchableOpacity
                onPress={() => console.log("Provide Journal Access PRESSED")}
              >
                <ListItems
                  IconComponent={
                    <MyIcon
                      name="notebook"
                      backgroundColor="#836fa9"
                      IconSize={50}
                    />
                  }
                  title="Provide Journal Access"
                  size={hp(15)}
                />
              </TouchableOpacity>
            </View>
            <View style={styles.listBackground}>
              <TouchableOpacity
                onPress={() => console.log("Request Appointment PRESSED")}
              >
                <ListItems
                  IconComponent={
                    <MyIcon
                      name="fountain-pen-tip"
                      backgroundColor="#836fa9"
                      IconSize={50}
                    />
                  }
                  title="Request Appointment"
                  size={hp(15)}
                />
              </TouchableOpacity>
            </View>
            <View style={styles.listBackground}>
              <TouchableOpacity
                onPress={() =>
                  console.log("Remove Therapist from list PRESSED")
                }
              >
                <ListItems
                  IconComponent={
                    <MyIcon
                      name="delete"
                      backgroundColor="#836fa9"
                      IconSize={50}
                    />
                  }
                  title="Remove Therapist from list"
                  size={hp(15)}
                />
              </TouchableOpacity>
            </View>
          </View>
        </Modal>
      </View>
    );
  }
}

const mapStateToProps = (state) => {
  return {
    ...state,
  };
};

export default connect(mapStateToProps, {})(TherapistList);
