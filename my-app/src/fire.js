import firebase from "firebase";

  var firebaseConfig = {
    apiKey: "AIzaSyB7I622egNymHdijv8Oa7TViKRYd-6m7P8",
    authDomain: "wealth42-assignment.firebaseapp.com",
    projectId: "wealth42-assignment",
    storageBucket: "wealth42-assignment.appspot.com",
    messagingSenderId: "209620124443",
    appId: "1:209620124443:web:f4906ed8e4e24a5e1c09be",
    measurementId: "G-W1HGEHRLG4"
  };
  // Initialize Firebase
  const fire = firebase.initializeApp(firebaseConfig);

  export default fire;