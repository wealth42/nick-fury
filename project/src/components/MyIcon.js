import React from "react";
import { View } from "react-native";

import { MaterialCommunityIcons } from "@expo/vector-icons";

export default function MyIcon({
  name,
  IconSize = 30,
  iconColor = "#fff",
  backgroundColor = "black",
}) {
  return (
    <View
      style={{
        borderRadius: IconSize / 2,
        alignItems: "center",
        justifyContent: "center",
        height: IconSize,
        width: IconSize,
        backgroundColor,
      }}
    >
      <MaterialCommunityIcons
        name={name}
        size={IconSize / 2}
        color={iconColor}
      />
    </View>
  );
}
