import React from 'react';
import './journalViewer.styles.scss';

import EmotionRecord from '../emotionRecord/emotionRecord.component';

const JournalViewer =({journal})=>(
    <div className="journal-box">
        <p className="date">Date : {journal.date}</p>
        <p className="content">{journal.name}</p>
        <EmotionRecord journal={journal}/>
    </div>
)

export default JournalViewer;