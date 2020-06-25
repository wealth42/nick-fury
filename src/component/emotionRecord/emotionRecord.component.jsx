import React, { Component } from 'react';
import Tag from '../../component/tag/tag.component';

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
    }

    wordCounter({journ, emotions, result}) {
        var blog = journ.name
        result = [];
        emotions.map(item => 
            item.words.map(word => 
                // blog.search(word)!==-1 ? count++ : null
                blog.search(word)!==-1 ? result.push(item.name) : null
        ))
        return result[0];
    }


    // {emotions.map(item => 
    //     item.words.map(word => {
    //         return <li>{word}</li>
    //     })
    // )}

    render() {
        var { journ, emotions, result } = this.state;
        journ = this.props.journal;
        var emo = this.wordCounter({journ, emotions, result});
        return(
            <div>
                <Tag emotionVal={emo} />
            </div>
        );
    }
}

export default EmotionRecord;