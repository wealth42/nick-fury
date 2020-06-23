import React, {Component} from 'react';
import {BrowserRouter, Route, Switch} from 'react-router-dom';
import './App.css';

import Dashboard from './pages/dashboard/dashboard.component';

class App extends Component {


  render() {
    return (
    <div>
      <BrowserRouter>
        <Switch>
          <Route exact path='/' component={Dashboard} />
        </Switch>
      </BrowserRouter>
    </div>
  );
  }
}

export default App;
