import React, { Component } from 'react';

class EmotionRecord extends Component {
    constructor() {
        super();
        this.state = {
            result: [],
            emotions:[],
            journ: []
        }
    }

    componentDidMount(){
        var data = require('../../assets/emotion.json')
        this.setState({
            emotions: data
        })
        var data1 = require('../../assets/journals.json')
        this.setState({
            journ: data1
        })
    }

    wordCounter({journ, emotions}) {
        var blog = [];
        var array = [];
        journ.map(item=>
            blog.push(item.name))
        console.log(blog);
        blog = blog[0];
        emotions.map(item => 
            item.words.map(word => 
                // blog.search(word)!==-1 ? count++ : null
                blog.search(word)!==-1 ? array.push(item.name) : null
        ))
        console.log(array);        
    }


    // {emotions.map(item => 
    //     item.words.map(word => {
    //         return <li>{word}</li>
    //     })
    // )}

    render() {
        const { journ, emotions } = this.state;
        this.wordCounter({journ, emotions});
        
        return(
            <div>
                <h2>Test Test Test</h2>
            </div>
        );
    }
}

export default EmotionRecord;