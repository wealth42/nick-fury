import { StyleSheet } from "react-native";
import {
  heightPercentageToDP as hp,
  widthPercentageToDP as wp,
} from "react-native-responsive-screen";
import colors from "./colors";

const styles = StyleSheet.create({
  authContainer: {
    flex: 1,
    backgroundColor: colors.lightGrey,
    alignItems: "center",
    paddingTop: hp("15"),
  },

  banner: {
    height: hp(15),
    width: hp(100),
    backgroundColor: colors.primaryViolet,
    alignItems: "center",
    justifyContent: "center",
  },

  bannerContainer: {
    alignItems: "center",
  },

  bannerTitle: {
    fontSize: 27,
    color: colors.white,
  },

  buttons: {
    alignItems: "center",
    marginTop: hp(5),
  },

  buttonText: {
    fontSize: 20,
    color: "white",
  },

  errorText: {
    color: "red",
    fontSize: 13,
    margin: wp(5),
  },

  forgotPassword: {
    fontSize: 17,
    fontStyle: "italic",
    textDecorationLine: "underline",
    marginVertical: hp(3),
  },

  homeContainer: {
    flex: 1,
    backgroundColor: colors.lightGrey,
    alignItems: "center",
  },

  homeTopbar: {
    flexDirection: "row",
    alignItems: "center",
    justifyContent: "center",
    height: hp(15),
    width: wp(100),
    backgroundColor: colors.primaryViolet,
    paddingTop: hp(1),
  },

  journalContainer: {
    height: hp(50),
    width: wp(90),
    borderRadius: 50,
    backgroundColor: colors.secondaryViolet,
    alignItems: "center",
    marginVertical: hp(6),
  },

  homeWelcomePlacement: {
    marginTop: hp(15),
    alignItems: "center",
  },

  listBackground: {
    backgroundColor: colors.secondaryViolet,
    elevation: 3,
    marginBottom: hp(5),
  },

  screenBackground: {
    backgroundColor: colors.lightGrey,
    flex: 1,
  },

  seperator: {
    height: hp(5),
  },

  subtitle: {
    fontSize: 20,
    marginVertical: hp("2"),
  },

  title: {
    fontSize: 30,
    color: colors.primaryViolet,
    marginVertical: hp("4"),
    textAlign: "center",
  },

  welcomeImage: {
    resizeMode: "contain",
    height: hp("40"),
    width: wp("80"),
  },
});

export default styles;
