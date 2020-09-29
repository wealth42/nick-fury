import React from "react";
import web from "../src/images/hero.png";
import Common from "./Common";

const About = () => {
    return (
        <>
        <Common 
        name='Welcome to About page'
        imgsrc={web}
        visit='/contact'
        btname="Contact Now"
        altname="about image"
        />
        </>
    );
};

export default About;
