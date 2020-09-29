import React from "react";
import web from "../src/images/img2.jpg";
import Common from "./Common";

const Home = () => {
    return (
        <>
        <Common
         name='Grow your business with'
        imgsrc={web}
        visit='/service'
        btname="Get Started"
        altname="home image"
         />
        </>
    );
};

export default Home;
