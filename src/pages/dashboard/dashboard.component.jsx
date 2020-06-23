import React, { Component } from 'react';
import KeySearch from '../../component/keySearch/keysearch.component';

class Dashboard extends Component{
    constructor(){
        super();
        this.state = {
            therapist:[]
        }
    }

    componentDidMount(){
        var data = require('../../assets/therapist.json')
        this.setState({
            therapist: data,
        })
    }

    render() {
        const { therapist }= this.state;
        return(
            <div>
                <h1>Welcome to Therapy </h1>
                <KeySearch 
                    placeholder="Enter Therapist Name"
                    therapist={therapist}
                />
            </div>
        );
    }
}

export default Dashboard;