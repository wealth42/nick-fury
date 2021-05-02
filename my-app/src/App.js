import React, {Fragment} from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Login from './components/auth/Login'

// import logo from './logo.svg';
import './App.css';

const App = () => (
  <Router>
    <Fragment>
      <Route exact path='/' component={Login} />
      
    </Fragment>
  </Router>
)



export default App;
