import React from 'react';
import './tag.styles.scss';

const Tag = ({emotionVal}) => (
    <div className="tag-space">
        <span className={(emotionVal==="Happiness")?"tag-box":"tag-box-another"}> {emotionVal} </span>
    </div>
);

export default Tag;