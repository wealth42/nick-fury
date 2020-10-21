import React, { useState } from "react";
import {
  View,
  StyleSheet,
  TouchableWithoutFeedback,
  Modal,
  FlatList,
  Text,
  TouchableOpacity,
} from "react-native";
import { MaterialCommunityIcons } from "@expo/vector-icons";
import { AppButton, Screen } from "./index";
import {
  heightPercentageToDP as hp,
  widthPercentageToDP as wp,
} from "react-native-responsive-screen";

function AppPicker({
  items,
  onSelectItem,
  placeholder,
  selectedItem,
  style,
  color,
  icon,
}) {
  const [modalVisible, setModalVisible] = useState(false);

  return (
    <View>
      <TouchableWithoutFeedback onPress={() => setModalVisible(true)}>
        <View style={[styles.container, style]}>
          {icon && (
            <MaterialCommunityIcons
              name={icon}
              size={20}
              style={styles.icon}
              color={color}
            />
          )}
          <Text style={styles.text}>
            {selectedItem ? selectedItem.label : placeholder}
          </Text>
        </View>
      </TouchableWithoutFeedback>
      <Modal visible={modalVisible} animationType="slide">
        <Screen>
          <View style={{ width: wp(100), alignItems: "center" }}>
            <AppButton
              text="Close"
              borderRadius={hp(100)}
              onPress={() => setModalVisible(false)}
              style={styles.buttons}
            />
          </View>
          <FlatList
            data={items}
            keyExtractor={(item) => item.value.toString()}
            renderItem={({ item }) => (
              <TouchableOpacity
                onPress={() => {
                  setModalVisible(false);
                  onSelectItem(item);
                }}
              >
                <Text style={{ padding: 25 }}>{item.label}</Text>
              </TouchableOpacity>
            )}
            contentContainerStyle={{ paddingBottom: 50 }}
          />
        </Screen>
      </Modal>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    backgroundColor: "#ebebeb",
    borderRadius: 25,
    flexDirection: "row",
    width: "100%",
    padding: 15,
    marginVertical: 10,
  },
  icon: {
    marginRight: 10,
  },
  text: {
    flex: 1,
  },
});

export default AppPicker;
