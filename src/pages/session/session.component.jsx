import React, { Component } from 'react';

import Chatbox from '../../component/chatbox/chatbox.component';
import PrivateNote from '../../component/privateNote/privateNote.component';
import LogIn from '../../component/login/login.component';

import './session.styles.scss'

class Session extends Component {
    constructor() {
        super();
        this.state={
            sessions:[]
        }
    }
    render() {
        const currentUser = this.props.currentUser;
        if (this.props.currentUser!==null) {
            var userInfo = this.props.currentUser.userType;
            console.log(userInfo);
        }
        return(
            <div>
            {currentUser===null ? <LogIn/>:
            <div className="main">
                <Chatbox/>
                <PrivateNote userInfo={userInfo}/>
            </div>}
            </div>
        );
    }
}
export default Session;