import React from 'react';
import './tag.styles.scss';

const Tag = ({emotionVal}) => (
    <div className="tag-space">
        <span className={(emotionVal==="Happiness")?"tag-box":(emotionVal==="Fear")?"tag-box-another":"tag-box-depressed"}> {emotionVal} </span>
    </div>
);

export default Tag;