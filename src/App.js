import React, {Component} from 'react';
import {BrowserRouter, Route, Switch} from 'react-router-dom';
import './App.css';

import Dashboard from './pages/dashboard/dashboard.component';
import EmotionRecord from './component/emotionRecord/emotionRecord.component';
import Journal from './pages/journal/journal.component';

class App extends Component {


  render() {
    return (
    <div>
      <BrowserRouter>
        <Switch>
          <Route exact path='/' component={Dashboard} />
          <Route exact path='/test' component={EmotionRecord} />
          <Route exact path='/journal' component={Journal} />
        </Switch>
      </BrowserRouter>
    </div>
  );
  }
}

export default App;
