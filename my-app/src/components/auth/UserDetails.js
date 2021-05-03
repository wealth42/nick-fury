import React, {Fragment, useState} from 'react'
import { Link } from 'react-router-dom'
import Camera from '../../img/Group 443.png'

import { Input, Button } from 'antd';

const UserDetails = () => {
    const [formData, setFormData] = useState({
        FirstName: '',
        LastName: '',
        City:'',
    });
    const uploadedImage = React.useRef(null);
    const imageUploader = React.useRef(null);

    const handleImageUpload = e => {
    const [file] = e.target.files;
    if (file) {
    const reader = new FileReader();
    const { current } = uploadedImage;
    current.file = file;
    reader.onload = e => {
      current.src = e.target.result;
    };
    reader.readAsDataURL(file);
  }
};
    const {  FirstName, LastName, City } = formData;
    const onChange = e => setFormData({ ...formData, [e.target.name]: e.target.value});
    const onSubmit = async e => {
        e.preventDefault();
            console.log('Success')
        }
    
    return (
        <Fragment>
            {/* <img className="Group7" src={Login1} alt=""/> */}
            <h1 className="large text-primary ConfirmDetails">Please confirm the details</h1>
            <h1 className="FetechImage">We have fetched this from google</h1>
            <input

            type="file"
            accept="image/*"
            onChange={handleImageUpload}
            ref={imageUploader}
            style={{
                display: "none",
                border:"none"
                }}
             />
            <div
            className="ImageContainer"
        onClick={() => imageUploader.current.click()}
      >
        <img
          ref={uploadedImage}
          style={{
            width: "100%",
            height: "100%",
            position: "absolute",
            border:"none"
          }}
          alt=""
        />
      </div>
            <svg className="upload"  onClick={() => imageUploader.current.click()} width="36" height="36" viewBox="0 0 36 36" fill="none" xmlns="http://www.w3.org/2000/svg">
<circle cx="18" cy="18" r="17" fill="#0E0E0E" stroke="white" stroke-width="2"/>
<path d="M24.9849 13.0019H22.2866L21.6438 11.2004C21.5994 11.0771 21.518 10.9706 21.4107 10.8953C21.3035 10.82 21.1756 10.7797 21.0446 10.7798H14.9576C14.6898 10.7798 14.4497 10.9484 14.3605 11.2004L13.7157 13.0019H11.0174C10.1405 13.0019 9.43018 13.7122 9.43018 14.5891V23.6362C9.43018 24.5131 10.1405 25.2234 11.0174 25.2234H24.9849C25.8618 25.2234 26.5721 24.5131 26.5721 23.6362V14.5891C26.5721 13.7122 25.8618 13.0019 24.9849 13.0019ZM18.0011 22.049C16.2473 22.049 14.8267 20.6284 14.8267 18.8746C14.8267 17.1207 16.2473 15.7001 18.0011 15.7001C19.755 15.7001 21.1756 17.1207 21.1756 18.8746C21.1756 20.6284 19.755 22.049 18.0011 22.049ZM16.0965 18.8746C16.0965 19.3797 16.2971 19.8642 16.6543 20.2214C17.0115 20.5786 17.496 20.7792 18.0011 20.7792C18.5063 20.7792 18.9907 20.5786 19.3479 20.2214C19.7051 19.8642 19.9058 19.3797 19.9058 18.8746C19.9058 18.3694 19.7051 17.885 19.3479 17.5278C18.9907 17.1706 18.5063 16.9699 18.0011 16.9699C17.496 16.9699 17.0115 17.1706 16.6543 17.5278C16.2971 17.885 16.0965 18.3694 16.0965 18.8746Z" fill="white"/>
</svg>
            <Input className="FirstName" type="email" placeholder="       First Name"/>
            <Input className="LastName" type="password"placeholder="       Last Name"/>
            <Input className="City" type="password"placeholder="       City"/>

            <h1 className="Terms">By signing up I agree to Terms and Conditions 
            & Privacy Policies</h1>

            <Button className="Next">
                    Next
            </Button>
            {/* <Button className="SignUp">
                    Sign up
            </Button>
            <h1 className="OrUsing">Or using</h1>
                <Button  className="Google"><img src={Google}/></Button>
                <Button className="Facebook"><img src={Facebook}/></Button> */}
        </Fragment>
    )
}
export default UserDetails;