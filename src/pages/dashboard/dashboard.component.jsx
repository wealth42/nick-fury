import React, { Component } from 'react';
import KeySearch from '../../component/keySearch/keysearch.component';
import LogIn from '../../component/login/login.component';
import './dashboard.styles.scss';

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
        // this.setState
        //     userInfo: "client"
            // userInfo: "therapist"

    }

    render() {
        var { therapist, clients }= this.state;
        if (this.props.currentUser!==null) {
            var userInfo = this.props.currentUser.userType;
            //console.log(userInfo);
        }
        var currentUser = this.props.currentUser;
        return(
            <div className="mainContent">
            {currentUser===null ? <LogIn/>:
            <div>
                <h1>Welcome to Therapy Aid</h1>
                <h3>India's largest online therapy platform for programmers</h3>
                <div className="search-box">
                {userInfo==="client" ? 
                    <KeySearch 
                    placeholder="Search for Therapists"
                    therapist={therapist}
                    />
                : null }
                {userInfo==="therapist" ?
                    <KeySearch 
                    placeholder="Search for Clients"
                    therapist={clients}
                    />: null}
                </div>
            </div>}
            </div>
        );
    }
}

export default Dashboard;