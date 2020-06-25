import React, { Component } from 'react';

import Chatbox from '../../component/chatbox/chatbox.component';
import Header from '../../component/header/header.component';
import PrivateNote from '../../component/privateNote/privateNote.component';

import './session.styles.scss'

class Session extends Component {
    constructor() {
        super();
        this.state={
            sessions:[]
        }
    }
    render() {
        return(
            <div>
                <Header/>
                <div className="main">
                <Chatbox/>
                <PrivateNote/>
                </div>
            </div>
        );
    }
}
export default Session;