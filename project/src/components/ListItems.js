import React from "react";
import { Image, Text, View } from "react-native";
import {
  heightPercentageToDP as hp
} from "react-native-responsive-screen";

function ListItems({
  size,
  title,
  subTitle,
  image,
  IconComponent,
  titleStyle,
  subTitleStyle,
  backgroundColor,
  page,
}) {
  return (
    <View
      style={{
        flexDirection: "row",
        alignItems: "center",
        height: size * 0.75,
        backgroundColor,
        padding: hp(4),
      }}
    >
      {IconComponent}
      {image && (
        <Image
          source={page ? image : { uri: image }}
          style={{
            height: size * 0.5,
            width: size * 0.5,
            borderRadius: size,
          }}
        />
      )}
      <View style={{ marginLeft: size * 0.15 }}>
        <Text style={[{ fontSize: size * 0.2 }, titleStyle]}>{title}</Text>
        {subTitle && (
          <Text style={[{ fontSize: size * 0.2 }, subTitleStyle]}>
            {subTitle}
          </Text>
        )}
      </View>
    </View>
  );
}

export default ListItems;
