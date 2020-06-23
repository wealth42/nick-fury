import React, { Component } from 'react';

class KeySearch extends Component {
    constructor(){
        super();
        this.state = {
            searchFields: ''
        }
    }
    render(){
        const {searchFields} = this.state;
        const filteredTherapist = this.props.therapist.filter(doctor =>
            doctor.name.toLowerCase().includes(searchFields.toLowerCase())
        );
        return( 
            <div>
            <input
                placeholder={this.props.placeholder}
                onChange={e=> this.setState({searchFields: e.target.value})}
            />
            <ul>
                {filteredTherapist.map(item => {
                return <li>{item.name}</li>;
                })}
            </ul>
            </div>
        );
    }
}

export default KeySearch;