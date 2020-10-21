import React from "react";
import { View, Text, StyleSheet } from "react-native";
import {
  widthPercentageToDP as wp,
  heightPercentageToDP as hp,
} from "react-native-responsive-screen";

function JournalList({ date, emotion, intensity, style }) {
  return (
    <View style={styles.container}>
      <View style={styles.border}>
        <Text style={style}>{date}</Text>
      </View>
      <View style={styles.border}>
        <Text style={style}>{emotion}</Text>
      </View>
      <View style={styles.border}>
        <Text style={style}>{intensity}</Text>
      </View>
    </View>
  );
}

export default JournalList;

const styles = StyleSheet.create({
  container: {
    flexDirection: "row",
  },

  border: {
    borderRightWidth: 1,
    borderColor: "black",
    paddingLeft: 20,
    width: wp("29%"),
    paddingVertical: 5,
    borderWidth: 1,
    marginTop: 10,
  },
});
