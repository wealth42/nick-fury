import React, { Component } from 'react';

import './privateNote.styles.scss';

class PrivateNote extends Component {
    constructor() {
        super();
        this.state={
            notes:[],
            tasks:[],
            // user: "client"
            //user: "therapist"
        }       
    }

    addItem({task}) {
        task.push()
    }

    render() {
        //var {notes} = this.state;
        const user = this.props.userInfo;
        return(
            <div className="note-box">
            {user==='therapist' ? 
                <div>
                <div className="message-box">
                    <ul>
                        <li>He is lazy to implement firebase</li>
                        <li>Need mentoring before working on project</li>
                    </ul>
                </div>
                <div className="insert">
                    <div>
                        <input className="text" type="text" placeholder="Any Personal Notes"/>
                        <button>Save</button>
                    </div>
                </div>
                </div>
                :
                null }
            {user==='therapist' ? 
                <div>
                <div className="message-box">
                    <ul>
                        <li>Read documentation before coding</li>
                        <li>Practice building more Apps</li>
                        <li>Try Meditation</li>
                    </ul>
                </div>
                <div className="insert">
                    <div>
                        <input className="text" type="text" placeholder="Assign Tasks"/>
                        <button>Assign</button>
                    </div>
                </div>
                </div>
                :
                <div>
                <h3>Task Assigned</h3>
                <div className="message-box">
                    <ul>
                        <li>Read documentation before coding</li>
                        <li>Practice building more Apps</li>
                        <li>Try Meditation</li>
                    </ul>
                </div>
                </div>}
            </div>
        );
    }
}
export default PrivateNote;