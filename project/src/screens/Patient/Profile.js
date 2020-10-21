import React, { Component } from "react";
import { connect } from "react-redux";
import { FlatList, View, Text, TouchableOpacity } from "react-native";
import {
  heightPercentageToDP as hp,
  widthPercentageToDP as wp,
} from "react-native-responsive-screen";

import { ListItems, MyIcon, ListItemSeparator } from "../../components";
import styles from "../../config/styles";

class Profile extends Component {
  constructor(props) {
    super(props);
    this.state = {
      profile: [
        {
          title: "Settings",
          size: 100,
          name: "settings-outline",
          backgroundColor: "#836fa9",
          IconSize: 50,
        },
        {
          title: "Credits",
          size: 100,
          name: "cash",
          backgroundColor: "#836fa9",
          IconSize: 50,
        },
      ],
    };
  }

  render() {
    return (
      <View style={styles.screenBackground}>
        <View style={styles.bannerContainer}>
          <View style={styles.banner}>
            <Text style={styles.bannerTitle}>Your Profile</Text>
          </View>
        </View>

        <View style={styles.listBackground}>
          <ListItems
            image={require("../../assets/AppLogo.png")}
            title={this.props.common.username}
            size={hp(30)}
            titleStyle={styles.subtitle}
            page="Profile"
          />
        </View>

        <View style={styles.listBackground}>
          <FlatList
            data={this.state.profile}
            keyExtractor={(item) => item.title}
            renderItem={({ item }) => (
              <TouchableOpacity onPress={() => console.log("press")}>
                <ListItems
                  IconComponent={
                    <MyIcon
                      name={item.name}
                      backgroundColor={item.backgroundColor}
                      IconSize={item.IconSize}
                    />
                  }
                  title={item.title}
                  size={item.size}
                />
              </TouchableOpacity>
            )}
            ItemSeparatorComponent={ListItemSeparator}
          />
        </View>

        <View style={styles.listBackground}>
          <TouchableOpacity onPress={() => this.props.navigation.popToTop()}>
            <ListItems
              IconComponent={
                <MyIcon name="logout" backgroundColor="#836fa9" IconSize={50} />
              }
              title="Logout"
              size={100}
            />
          </TouchableOpacity>
        </View>
      </View>
    );
  }
}

const mapStateToProps = (state) => {
  return {
    ...state,
  };
};

export default connect(mapStateToProps, {})(Profile);
