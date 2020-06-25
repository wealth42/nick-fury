import React, { Component } from 'react';

import './chatbox.styles.scss'

class Chatbox extends Component {
    constructor() {
        super();
        this.state={
            chats:[]
        }       
    }

    componentDidMount() {
        var data = require('../../assets/chats.json')
        this.setState({
            chats: data
        })
    }

    render() {
        var {chats} = this.state;
        return(
            <div className="chat-box">
                <div className="scroll-content">
                {chats.map(message=> 
                    <div>
                    <p className="from">{message.sender}</p>
                    <div className="message-box">
                        <p>{message.text} </p>
                        <p className="time">Sent on : {message.time}</p>
                    </div>
                    </div>
                )}
                </div>
                <input className="text" type="textbox" placeholder="Enter your message"/>
                <button>Send</button>
            </div>
        );
    }
}
export default Chatbox;