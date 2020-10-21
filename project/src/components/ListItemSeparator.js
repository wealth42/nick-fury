import React from "react";
import { StyleSheet, View } from "react-native";

function ListItemSeparator() {
  return <View style={styles.listSeparator} />;
}

const styles = StyleSheet.create({
  listSeparator: {
    width: "95%",
    height: 1,
    left: "2.5%",
    backgroundColor: "#a094b7",
  },
});

export default ListItemSeparator;
