import React, { Component } from 'react';
import KeySearch from '../../component/keySearch/keysearch.component';

import Header from '../../component/header/header.component';

class Dashboard extends Component{
    constructor(){
        super();
        this.state = {
            therapist:[],
            clients: [],
            userInfo: []
        }
    }

    componentDidMount(){
        var data = require('../../assets/therapist.json')
        this.setState({
            therapist: data,
        })
        var data1 = require('../../assets/clients.json')
        this.setState({
            clients: data1,
        })
        this.setState({
            userInfo: "client"
            // userInfo: "therapist"
        })
    }

    render() {
        var { therapist, userInfo, clients }= this.state;
        return(
            <div>
                <Header currentUser={false}/>
                <h1>Welcome to Therapy </h1>
                {userInfo==="client" ? 
                    <KeySearch 
                    placeholder="Search for Therapists"
                    therapist={therapist}
                    />
                :
                    <KeySearch 
                    placeholder="Search for Clients"
                    therapist={clients}
                    />
                }
            </div>
        );
    }
}

export default Dashboard;