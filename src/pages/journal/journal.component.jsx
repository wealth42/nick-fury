import React, { Component } from 'react';

import Header from '../../component/header/header.component';
import JournalViewer from '../../component/journalViewer/journalViewer.component';

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
    

    render() {
        const {journ} = this.state;
        return(
            <div>
                <Header currentUser={false}/>
                {journ.map(journal => <JournalViewer journal={journal}/>)}

            </div>
        );
    }
}

export default Journal;