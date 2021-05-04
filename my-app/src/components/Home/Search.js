import React, {Fragment} from 'react'
// import { Button} from 'antd';
import {Button} from 'react-bootstrap'
import search from '../../img/Search Glyph   Light.svg'
import heart from '../../img/Heart.png'
import Nheart from '../../img/nonheart.svg'
import Footer from '../Layout/Footer'
import Header from '../Layout/Header'
// import button from "bootstrap"
//  const { Meta } = Card;
const Search = () => {
    return(
        <Fragment>
            <Header>
                <div>
                    <h1 className="HeaderText">Search</h1>
                </div>
                
            </Header>
            <Button className="SearchTherapist" style={{border:"none"}}>
                <img className="SearchIcon" alt="" src={search}></img>
                <span className="searchtextTherapist">Search in therapist</span>
            </Button>
            <div className="SearchCardOne">
                <div>
                    <div style={{position:"absolute",left:"16px",top:"18%"}}>
                    <svg  width="57" height="57" viewBox="0 0 57 57" fill="none" xmlns="http://www.w3.org/2000/svg">
<circle cx="28.5" cy="28.5" r="28.5" fill="#C4C4C4"/>
</svg>
                    </div>

                </div>
                <div className="col-md-8">
                    <div className="card-body">
                        <p className="Name" >
                            Andrew Parker
                        </p>
                        <div>
                            <img className="heart" alt="" src={heart}/>
                        </div>  
                        <div>
                            <p className="card-text">
                                Description Description 
                                24th May 2:02PM
                            </p>
                        </div>
                        <div>
                            <p className="card-text1">
                                 View Details 
                                 <Button variant="outline-success" style={{
                                display: "flex",
                                flexDirection: "row",
                                justifyContent: "center",
                                alignItems: "center",
                                padding: "7px 32px",
                                
                                width: "60.52px",
                                height: "20px",
                                left: "311px",
                                top: "279px",
                                marginTop: "-19px",
                                marginLeft: "187px",
                                border: "1px solid #2BFEBA",
                                boxSizing: "border-box",
                                borderRadius: "15px",
                                fontWeight: "normal",
                                fontSize: "12px",
                                lineHeight: "132.5%",
                                color:"#2BFEBA"
                            }}>
                                Book
                            </Button>{''}
                            </p>
                            
                        </div>
                        
                    </div>
                    
                    
                </div>

            </div>
            <div className="SearchCardTwo">
                <div>
                    <div style={{position:"absolute",left:"16px",top:"18%"}}>
                    <svg  width="57" height="57" viewBox="0 0 57 57" fill="none" xmlns="http://www.w3.org/2000/svg">
<circle cx="28.5" cy="28.5" r="28.5" fill="#C4C4C4"/>
</svg>
                    </div>

                </div>
                <div className="col-md-8">
                    <div className="card-body">
                        <p className="Name" >
                            Andrew Parker
                        </p>
                        <div>
                            <img className="heart" alt="" src={Nheart}/>
                        </div>  
                        <div>
                            <p className="card-text">
                                Description Description 
                                24th May 2:02PM
                            </p>
                        </div>
                        <div>
                            <p className="card-text1">
                                 View Details 
                                 <Button variant="outline-success" style={{
                                display: "flex",
                                flexDirection: "row",
                                justifyContent: "center",
                                alignItems: "center",
                                padding: "7px 32px",
                                
                                width: "60.52px",
                                height: "20px",
                                left: "311px",
                                top: "279px",
                                marginTop: "-19px",
                                marginLeft: "187px",
                                border: "1px solid #2BFEBA",
                                boxSizing: "border-box",
                                borderRadius: "15px",
                                fontWeight: "normal",
                                fontSize: "12px",
                                lineHeight: "132.5%",
                                color:"#2BFEBA"
                            }}>
                                Book
                            </Button>{''}
                            </p>
                            
                        </div>
                        
                    </div>
                    
                    
                </div>

            </div>
            <div className="SearchCardThree">
                <div>
                    <div style={{position:"absolute",left:"16px",top:"18%"}}>
                    <svg  width="57" height="57" viewBox="0 0 57 57" fill="none" xmlns="http://www.w3.org/2000/svg">
<circle cx="28.5" cy="28.5" r="28.5" fill="#C4C4C4"/>
</svg>
                    </div>

                </div>
                <div className="col-md-8">
                    <div className="card-body">
                        <p className="Name" >
                            Andrew Parker
                        </p>
                        <div>
                            <img className="heart" alt="" src={heart}/>
                        </div>  
                        <div>
                            <p className="card-text">
                                Description Description 
                                24th May 2:02PM
                            </p>
                        </div>
                        <div>
                            <p className="card-text1">
                                 View Details 
                                 <Button variant="outline-success" style={{
                                display: "flex",
                                flexDirection: "row",
                                justifyContent: "center",
                                alignItems: "center",
                                padding: "7px 32px",
                                
                                width: "60.52px",
                                height: "20px",
                                left: "311px",
                                top: "279px",
                                marginTop: "-19px",
                                marginLeft: "187px",
                                border: "1px solid #2BFEBA",
                                boxSizing: "border-box",
                                borderRadius: "15px",
                                fontWeight: "normal",
                                fontSize: "12px",
                                lineHeight: "132.5%",
                                color:"#2BFEBA"
                            }}>
                                Book
                            </Button>{''}
                            </p>
                            
                        </div>
                        
                    </div>
                    
                    
                </div>

            </div>
            <div className="SearchCardFour">
                <div>
                    <div style={{position:"absolute",left:"16px",top:"18%"}}>
                    <svg  width="57" height="57" viewBox="0 0 57 57" fill="none" xmlns="http://www.w3.org/2000/svg">
<circle cx="28.5" cy="28.5" r="28.5" fill="#C4C4C4"/>
</svg>
                    </div>

                </div>
                <div className="col-md-8">
                    <div className="card-body">
                        <p className="Name" >
                            Andrew Parker
                        </p>
                        <div>
                            <img className="heart" alt="" src={heart}/>
                        </div>  
                        <div>
                            <p className="card-text">
                                Description Description 
                                24th May 2:02PM
                            </p>
                        </div>
                        <div>
                            <p className="card-text1">
                                 View Details 
                                 <Button variant="outline-success" style={{
                                display: "flex",
                                flexDirection: "row",
                                justifyContent: "center",
                                alignItems: "center",
                                padding: "7px 32px",
                                
                                width: "60.52px",
                                height: "20px",
                                left: "311px",
                                top: "279px",
                                marginTop: "-19px",
                                marginLeft: "187px",
                                border: "1px solid #2BFEBA",
                                boxSizing: "border-box",
                                borderRadius: "15px",
                                fontWeight: "normal",
                                fontSize: "12px",
                                lineHeight: "132.5%",
                                color:"#2BFEBA"
                            }}>
                                Book
                            </Button>{''}
                            </p>
                            
                        </div>
                        
                    </div>
                    
                    
                </div>

            </div>
            <Footer>
               
            </Footer>
        </Fragment>
    )
}
export default Search;