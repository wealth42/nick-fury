import React, {Fragment, useState} from 'react'
import { Button, Tooltip, Card,Input } from 'antd';
import { SearchOutlined } from '@ant-design/icons';
import search from '../../img/Search Glyph   Light.svg'
import filter from '../../img/filtrr.svg'
import Footer from '../Layout/Footer'
const { Meta } = Card;
const HomeNotes = () => {
    return(
    <Fragment >
            <Button className="Search" ><img className="SearchIcon" alt="" src={search}></img><span className="searchtext">Search in Journal</span></Button>
           <img  className="filter" src={filter} alt=""></img>

            <Card className="cardone"
                style={{ width: 300 }}
               
                
            >
                <div className="cardImage"
                  
                />
                
                <Meta
                
                title="Headline" 
                style={{
                    position:"absolute",
                    width: "76px",
                    height: "23px",
                    left: "13.72px",
                    top: "178.82px",
                    fontStyle: "normal",
                    fontWeight: "bold",
                    fontSize: "18px",
                    lineHeight: "125%",
                    
                    
                    color: "#FFFFFF"}}
                
                />
                <Meta description="Description Description Description Description Description Description"  style={{
                     position:"absolute",
                    width: "288.56px",
                    height: "40px",
                    left: "13.72px",
                    top: "202.82px",
                    fontStyle: "normal",
                    fontWeight: "normal",
                    fontSize: "14px",
                    lineHeight: "140.2%",
                    
                    
                    color: "#FFFFFF"}} />
                <Meta description="Feeling" style={{
                    position:"absolute",
                    width: "76.56px",
                    height: "17.37px",
                    left: "13.72px",
                    bottom: "14.82px",
                    fontStyle: "normal",
                    fontWeight: "normal",
                    fontSize: "12px",
                    lineHeight: "140.2%",
                    
                    
                    color: "#797980"}}/>
                <Meta description="Date" style={{
                    position:"absolute",
                    width: "120.56px",
                    height: "17.37px",
                    left: "130.33px",
                    bottom: "14.73px",
                    fontStyle: "normal",
                    fontWeight: "normal",
                    fontSize: "12px",
                    lineHeight: "140.2%",
                    
                    
                    color: "#797980"}}/>
                

            </Card>
            <Card className="cardtwo"
                style={{ width: 300 }}
               
                
            >
                <div className="cardImage"
                  
                />
                
                <Meta
                
                title="Headline" 
                style={{
                    position:"absolute",
                    width: "76px",
                    height: "23px",
                    left: "13.72px",
                    top: "178.82px",
                    fontStyle: "normal",
                    fontWeight: "bold",
                    fontSize: "18px",
                    lineHeight: "125%",
                    
                    
                    color: "#FFFFFF"}}
                
                />
                <Meta description="Description Description Description Description Description Description"  style={{
                     position:"absolute",
                    width: "288.56px",
                    height: "40px",
                    left: "13.72px",
                    top: "202.82px",
                    fontStyle: "normal",
                    fontWeight: "normal",
                    fontSize: "14px",
                    lineHeight: "140.2%",
                    
                    
                    color: "#FFFFFF"}} />
                <Meta description="Feeling" style={{
                    position:"absolute",
                    width: "76.56px",
                    height: "17.37px",
                    left: "13.72px",
                    bottom: "14.82px",
                    fontStyle: "normal",
                    fontWeight: "normal",
                    fontSize: "12px",
                    lineHeight: "140.2%",
                    
                    
                    color: "#797980"}}/>
                <Meta description="Date" style={{
                    position:"absolute",
                    width: "120.56px",
                    height: "17.37px",
                    left: "130.33px",
                    bottom: "14.73px",
                    fontStyle: "normal",
                    fontWeight: "normal",
                    fontSize: "12px",
                    lineHeight: "140.2%",
                    
                    
                    color: "#797980"}}/>
                

            </Card>
            <Footer/>
    </Fragment>
    )
    
}

export default HomeNotes;