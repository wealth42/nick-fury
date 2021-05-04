import React, {Fragment, useState, useEffect} from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Login from './components/auth/Login'
import UserDetails from './components/auth/UserDetails'
import HomeNotes from './components/Home/HomeNotes'
import Search from './components/Home/Search'

// import logo from './logo.svg';
import './App.css';

const App = () => (
  <Router>
    <Fragment>
      <Route exact path='/' component={Login} />
      <Route exact path='/UserDetails'component={UserDetails}/>
      <Route exact path='/HomeNotes'component={HomeNotes}/>
      <Route exact path='/Search'component={Search}/>

    </Fragment>
  </Router>
)



export default App;
