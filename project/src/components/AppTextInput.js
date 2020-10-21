import React from "react";
import { StyleSheet, TextInput, View } from "react-native";
import { MaterialCommunityIcons } from "@expo/vector-icons";

export default function AppTextInput({
  icon,
  iconcolor,
  size,
  style,
  ...otherProps
}) {
  return (
    <View
      style={[
        {
          flexDirection: "row",
          width: "80%",
          padding: size / 2.5,
          backgroundColor: "#ebebeb",
          borderRadius: size,
          alignItems: "center",
          marginVertical: 10,
        },
        style,
      ]}
    >
      {icon && (
        <MaterialCommunityIcons
          name={icon}
          size={size * 1.2}
          color={iconcolor}
          style={styles.icon}
        />
      )}
      <TextInput {...otherProps} />
    </View>
  );
}

const styles = StyleSheet.create({
  icon: {
    marginHorizontal: 10,
  },
});
