import React, {Component} from 'react';
import {BrowserRouter, Route, Switch} from 'react-router-dom';
import './App.css';

import Dashboard from './pages/dashboard/dashboard.component';
import Journal from './pages/journal/journal.component';
import Session from './pages/session/session.component';
import Header from './component/header/header.component';
import LogInSignUp from './pages/login-signup/login-signup.component';
import { auth, createUserProfileDocument } from './firebase/firebase.utils';

class App extends Component {
  constructor() {
    super();
    this.state = {
      currentUser: null
    }
  }
  unsubscribeFromAuth = null;

  componentDidMount() {
    this.unsubscribeFromAuth = auth.onAuthStateChanged(async userAuth => {
      if (userAuth) {
        const userRef = await createUserProfileDocument(userAuth);

        userRef.onSnapshot(snapShot => {
          this.setState({
            currentUser: {
              id: snapShot.id,
              ...snapShot.data()
            }
          });
        });
      }
      else{
      this.setState({currentUser: userAuth});
      }
    });
  }

  componentWillUnmount() {
    this.unsubscribeFromAuth();
  }

  render() {
    const {currentUser} = this.state;
    //console.log(currentUser);
    return (
    <div className="content">
      <BrowserRouter>
        <Header currentUser={this.state.currentUser}/>
        <Switch>
          <Route exact path='/' render={() => (<Dashboard currentUser={currentUser} />)}/>
          <Route exact path='/signin' component={LogInSignUp} />
          <Route exact path='/journal' render={() => (<Journal currentUser={currentUser} />)}/>
          <Route exact path='/session' render={() => (<Session currentUser={currentUser} />)}/>
        </Switch>
      </BrowserRouter>
    </div>
  );
  }
}

export default App;
