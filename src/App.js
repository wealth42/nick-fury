import React, {Component} from 'react';
import {BrowserRouter, Route, Switch} from 'react-router-dom';
import './App.css';

import Dashboard from './pages/dashboard/dashboard.component';
import PrivateNote from './component/privateNote/privateNote.component';
import Journal from './pages/journal/journal.component';
import Session from './pages/session/session.component';

class App extends Component {


  render() {
    return (
    <div>
      <BrowserRouter>
        <Switch>
          <Route exact path='/' component={Dashboard} />
          <Route exact path='/test' component={PrivateNote} />
          <Route exact path='/journal' component={Journal} />
          <Route exact path='/session' component={Session} />
        </Switch>
      </BrowserRouter>
    </div>
  );
  }
}

export default App;
