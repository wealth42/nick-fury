import moment from "moment";
import React, { Component } from "react";
import {
  heightPercentageToDP as hp,
  widthPercentageToDP as wp,
} from "react-native-responsive-screen";
import { connect } from "react-redux";

import { FlatList, View, Modal, Text } from "react-native";
import { AppButton, AppPicker } from "../../components";
import styles from "../../config/styles";

export class Journal extends Component {
  constructor(props) {
    super(props);
    this.state = {
      emotionCategories: [
        { label: "Happiness", value: 1 },
        { label: "Caring", value: 2 },
        { label: "Depression", value: 3 },
        { label: "Inadequate", value: 4 },
        { label: "Fear", value: 5 },
        { label: "Confusion", value: 6 },
        { label: "Hurt", value: 7 },
        { label: "Anger", value: 8 },
        { label: "Lonliness", value: 9 },
        { label: "Remorse", value: 10 },
      ],
      intensityCategories: [
        { label: "Strong", value: 1 },
        { label: "Medium", value: 2 },
        { label: "Light", value: 3 },
      ],
      modalVisible: false,
      entries: [],
      emotion: "",
      intensity: "",
    };
  }

  entries() {
    let { entries, intensity, emotion } = this.state;
    let now = moment().format("lll");
    entries.push(now + "  " + emotion.label + "   " + intensity.label);
    this.setState({
      entries,
      modalVisible: false,
    });
  }

  render() {
    return (
      <View style={styles.homeContainer}>
        <View style={styles.bannerContainer}>
          <View style={styles.banner}>
            <Text style={styles.bannerTitle}>Your Journal</Text>
          </View>
        </View>
        <View style={styles.journalContainer}>
          <FlatList
            data={this.state.entries}
            renderItem={({ item }) => <Text>{item}</Text>}
          />
        </View>

        <AppButton
          borderRadius={wp(100)}
          text="Make an entry"
          onPress={() => this.setState({ modalVisible: true })}
        />

        <Modal
          visible={this.state.modalVisible}
          onRequestClose={() => this.setState({ modalVisible: false })}
          animationType={"slide"}
        >
          <View style={styles.homeContainer}>
            <View style={styles.banner}>
              <Text style={styles.bannerTitle}>
                Please describe the following
              </Text>
            </View>
            <Text style={styles.subtitle}>
              What emotion are you feeling right now?
            </Text>

            <AppPicker
              selectedItem={this.state.emotion}
              onSelectItem={(item) => this.setState({ emotion: item })}
              items={this.state.emotionCategories}
              placeholder="Category"
            />
            <Text style={styles.subtitle}>Please select the intensity</Text>

            <AppPicker
              selectedItem={this.state.intensity}
              onSelectItem={(item) => this.setState({ intensity: item })}
              items={this.state.intensityCategories}
              placeholder="Intensity"
            />

            <AppButton
              text="Add Entry"
              borderRadius={hp(100)}
              onPress={() => this.entries()}
              style={styles.buttons}
            />
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

export default connect(mapStateToProps, {})(Journal);
