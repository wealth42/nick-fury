import firebase from 'firebase/app';
import 'firebase/firestore';
import 'firebase/auth';

const config = 
{apiKey: "AIzaSyDM8I7-tZi2nVpE-uZuCNe2Cn0lnFToelU",
authDomain: "nick-fury-69744.firebaseapp.com",
databaseURL: "https://nick-fury-69744.firebaseio.com",
projectId: "nick-fury-69744",
storageBucket: "nick-fury-69744.appspot.com",
messagingSenderId: "514296784522",
appId: "1:514296784522:web:6fe8569f69d60937416f73",
measurementId: "G-RYGM7TV1Y9"}

firebase.initializeApp(config);

export const createUserProfileDocument = async (userAuth, additionalData) => {
    if (!userAuth) return;
  
    const userRef = firestore.doc(`users/${userAuth.uid}`);
  
    const snapShot = await userRef.get();
  
    if (!snapShot.exists) {
      const { displayName, email } = userAuth;
      const createdAt = new Date();
      try {
        await userRef.set({
          displayName,
          email,
          createdAt,
          ...additionalData
        });
      } catch (error) {
        console.log('error creating user', error.message);
      }
    }
    return userRef;
  };

export const auth = firebase.auth();
export const firestore = firebase.firestore();
const provider = new firebase.auth.GoogleAuthProvider();
provider.setCustomParameters({ prompt: 'select_account' });
export const signInWithGoogle = () => auth.signInWithPopup(provider);

export default firebase;