import React, {Fragment} from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Login from './components/auth/Login'
import UserDetails from './components/auth/UserDetails'

// import logo from './logo.svg';
import './App.css';

const App = () => (
  <Router>
    <Fragment>
      <Route exact path='/Login' component={Login} />
      <Route exact path='/UserDetails'component={UserDetails}/>
    </Fragment>
  </Router>
)



export default App;
