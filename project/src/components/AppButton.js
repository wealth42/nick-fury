import React from "react";
import { StyleSheet, Text, TouchableOpacity, View } from "react-native";
import {
  heightPercentageToDP as hp,
  widthPercentageToDP as wp
} from "react-native-responsive-screen";

export default function AppButton({
  text,
  height = hp("6"),
  width = wp("80"),
  backgroundColor = "#5e35b1",
  borderRadius,
  style,
  txtstyle,
  onPress,
}) {
  return (
    <TouchableOpacity onPress={onPress}>
      <View
        style={[
          {
            alignItems: "center",
            justifyContent: "center",
            height,
            width,
            backgroundColor,
            borderRadius,
          },
          style,
        ]}
      >
        <Text style={[{ color: "#fff", fontSize: 20 }, txtstyle]}>{text}</Text>
      </View>
    </TouchableOpacity>
  );
}

const styles = StyleSheet.create({});
