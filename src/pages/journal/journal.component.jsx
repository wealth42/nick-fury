import React, { Component } from 'react';

import JournalViewer from '../../component/journalViewer/journalViewer.component';
import LogIn from '../../component/login/login.component';

class Journal extends Component {
    constructor() {
        super();
        this.state = {
            journ:[]
        }
    }
    
    componentDidMount() {
        var data1 = require('../../assets/journals.json')
        this.setState({
            journ: data1
        })
    }
    
//{journ.map(journal => <JournalViewer journal={journal}/>)}
    render() {
        const {journ} = this.state;
        const currentUser = this.props.currentUser;
        return(
            <div>
                {currentUser===null ?
                <div>
                    <LogIn/>
                </div>
                :
                <div>
                    {journ.map(journal => <JournalViewer journal={journal}/>)}
                </div>
                }
            </div>
        );
    }
}

export default Journal;