import React from "react";

import { NavigationContainer } from "@react-navigation/native";
import { createStackNavigator } from "@react-navigation/stack";
import { createBottomTabNavigator } from "@react-navigation/bottom-tabs";

import { MaterialCommunityIcons } from "@expo/vector-icons";

import {
  Welcome,
  PatientLogin,
  TherapistLogin,
  PatientSignup,
  TherapistSignup,
} from "./screens/Auth"; //Importing all authentication pages

import {
  Journal,
  PatientHome,
  Profile,
  TherapistList,
} from "./screens/Patient";

const authNav = createStackNavigator();
function authStackNav() {
  return (
    <authNav.Navigator
      screenOptions={{
        headerShown: false,
      }}
    >
      <authNav.Screen name="Welcome" component={Welcome} />
      <authNav.Screen name="PatientLogin" component={PatientLogin} />
      <authNav.Screen name="TherapistLogin" component={TherapistLogin} />
      <authNav.Screen name="PatientSignup" component={PatientSignup} />
      <authNav.Screen name="TherapistSignup" component={TherapistSignup} />
    </authNav.Navigator>
  );
}

const patientNav = createBottomTabNavigator();
function patientTabNav() {
  return (
    <patientNav.Navigator
      tabBarOptions={{
        activeBackgroundColor: "#9162e4",
        activeTintColor: "#fff",
        inactiveTintColor: "#a094b7",
      }}
    >
      <patientNav.Screen
        name="PatientHome"
        component={PatientHome}
        options={{
          tabBarLabel: "Home",
          tabBarIcon: ({ color, size }) => (
            <MaterialCommunityIcons name="home" color={color} size={size} />
          ),
        }}
      />
      <patientNav.Screen
        name="Journal"
        component={Journal}
        options={{
          tabBarLabel: "Journal",
          tabBarIcon: ({ color, size }) => (
            <MaterialCommunityIcons name="notebook" color={color} size={size} />
          ),
        }}
      />
      <patientNav.Screen
        name="TherapistList"
        component={TherapistList}
        options={{
          tabBarLabel: "TherapistList",
          tabBarIcon: ({ color, size }) => (
            <MaterialCommunityIcons
              name="account-group"
              color={color}
              size={size}
            />
          ),
        }}
      />
      <patientNav.Screen
        name="Profile"
        component={Profile}
        options={{
          tabBarLabel: "Profile",
          tabBarIcon: ({ color, size }) => (
            <MaterialCommunityIcons name="account" color={color} size={size} />
          ),
        }}
      />
    </patientNav.Navigator>
  );
}

const rootStack = createStackNavigator();
export default function () {
  return (
    <NavigationContainer>
      <rootStack.Navigator
        screenOptions={{
          headerShown: false,
        }}
      >
        <rootStack.Screen name="Auth" component={authStackNav} />
        <rootStack.Screen name="Patient" component={patientTabNav} />
      </rootStack.Navigator>
    </NavigationContainer>
  );
}
