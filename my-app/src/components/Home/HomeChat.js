import React, {Fragment} from 'react'
import oval from '../../img/Oval.png'
import oval1 from '../../img/Oval1.png'
import oval2 from '../../img/Oval2.png'
import oval3 from '../../img/oval3.png'
import Shape from '../../img/Shape.png'
import {Link} from 'react-router-dom'
import Footer from '../Layout/Footer'




const HomeChat =()=> {
    return (
       <Fragment>
           <div className="HomeChatHeader">
                <h1 className="HeaderText">
                    Chat
                </h1>
                <img alt="" src={oval} className="HeaderImage"/>
           </div>
           <card className="chatbox1">
               <img alt="" src={oval1} className="Chat1" />
                <div className="card-body">
                    <p className="chatname">
                    Andrew Parker
                    </p>
                    <p className="chatDes">
                    Hey Bill!
                    </p>
                    <p className="LastSeen">
                        9:48 PM
                    </p>
                   {/* <img alt="" src={Shape} className="SeeChat" /> Bad Quality */}
                   <Link>
                   <svg className="SeeChat" width="9" height="14" viewBox="0 0 9 14" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M5.51727 6.99997L0.789369 11.757C0.359273 12.1897 0.359273 12.8913 0.789369 13.3241C1.21947 13.7568 1.91679 13.7568 2.34689 13.3241L7.85354 7.78352C8.28364 7.35078 8.28364 6.64916 7.85354 6.21642L2.34689 0.675876C1.91679 0.243133 1.21947 0.243133 0.789369 0.675876C0.359273 1.10862 0.359273 1.81023 0.789369 2.24298L5.51727 6.99997Z" fill="white" fill-opacity="0.3"/>
</svg></Link>
                    {/* SVG looks better */}
                </div>
            </card>
           <card className="chatbox2">
               <img alt="" src={oval2} className="Chat2" />
               <div className="card-body">
                    <p className="chatname">
                    Karen Castillo
                    </p >
                    
                    <p className="chatDes">
                    Thank you ma’am
                    </p>
                    <p className="LastSeen">
                       7:08 PM
                    </p>
                    <Link>
                    <svg className="SeeChat" width="9" height="14" viewBox="0 0 9 14" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M5.51727 6.99997L0.789369 11.757C0.359273 12.1897 0.359273 12.8913 0.789369 13.3241C1.21947 13.7568 1.91679 13.7568 2.34689 13.3241L7.85354 7.78352C8.28364 7.35078 8.28364 6.64916 7.85354 6.21642L2.34689 0.675876C1.91679 0.243133 1.21947 0.243133 0.789369 0.675876C0.359273 1.10862 0.359273 1.81023 0.789369 2.24298L5.51727 6.99997Z" fill="white" fill-opacity="0.3"/>
</svg></Link>
                </div>
            </card>
           <card className="chatbox3">
               <img alt="" src={oval3} className="Chat3" />
               <div className="card-body">
                    <p className="chatname">
                    Martha Craig
                    </p>
                    <p className="chatDes">
                    Hey I am feeling..
                    </p>
                    <p className="LastSeen">
                        Monday
                    </p>
                    <Link>
                    <svg className="SeeChat" width="9" height="14" viewBox="0 0 9 14" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M5.51727 6.99997L0.789369 11.757C0.359273 12.1897 0.359273 12.8913 0.789369 13.3241C1.21947 13.7568 1.91679 13.7568 2.34689 13.3241L7.85354 7.78352C8.28364 7.35078 8.28364 6.64916 7.85354 6.21642L2.34689 0.675876C1.91679 0.243133 1.21947 0.243133 0.789369 0.675876C0.359273 1.10862 0.359273 1.81023 0.789369 2.24298L5.51727 6.99997Z" fill="white" fill-opacity="0.3"/>
</svg></Link>
                </div>
            </card>
           <Footer />
         
       </Fragment>
    )
}
export default HomeChat;