import React, { Component } from 'react';
import './keysearch.styles.scss'

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
            <div className="keyfield">
            <input
                className="textinput"
                placeholder={this.props.placeholder}
                onChange={e=> this.setState({searchFields: e.target.value})}
            />
            {filteredTherapist.map(item => {
            return <div>{item.name}</div>;
            })}
            </div>
        );
    }
}

export default KeySearch;