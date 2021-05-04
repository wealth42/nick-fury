import React from 'react'
import {Link} from 'react-router-dom'
import {Button} from 'react-bootstrap'
import chat from '../../img/chat.png'
import search from '../../img/Calender.png'
import home from '../../img/hoomee.png'


const Footer = () => {
    return (
        <div className="footer" style={{
            display: "flex",
            flexDirection: "row",
            justifyContent: "space-around",
            alignItems: "stretch",
            alignContent: "center",
            flexWrap:" wrap",
            }}> 
                <Link to="/HomeNotes"><Button className="HomeB"><img alt="" src={home}/></Button></Link>
                <Link to="/Search"><Button className="SearchB"><img alt="" src={search}/></Button></Link> 
                <Link to="/"><Button className="ChatB"><img alt="" src={chat}/></Button></Link> 
        </div>
    )
}

export default Footer;
