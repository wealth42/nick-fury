import React, {useState} from 'react'
import {Link} from 'react-router-dom'
import {Button} from 'react-bootstrap'
import chat from '../../img/chat.png'
import search from '../../img/Calender.png'
import home from '../../img/hoomee.png'
import GreenC from '../../img/GreenCalender.png'


const Footer = () => {
const active = <img alt="" src={GreenC}></img>
const normal = <img alt="" src={search}></img>
    
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
                <Link to="/Search"><Button onClick={this.src={active}} className="SearchB"><img alt="" src={normal}/></Button></Link> 
                <Link to="/"><Button className="ChatB"><img alt="" src={chat}/></Button></Link> 
        </div>
    )
}

export default Footer;
