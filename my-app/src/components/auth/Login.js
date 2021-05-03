import React, {Fragment, useState} from 'react'
import { Link } from 'react-router-dom'
import Login1 from '../../img/Group 7.svg'
import Google from '../../img/google.svg'
import Facebook from '../../img/facebook.svg'
import { Input, Button } from 'antd';
import ButtonGroup from '@material-ui/core/ButtonGroup';

const Login = () => {
    const [formData, setFormData] = useState({
        email: '',
        password: '',
    });

    const {  email, password } = formData;
    const onChange = e => setFormData({ ...formData, [e.target.name]: e.target.value});
    const onSubmit = async e => {
        e.preventDefault();
            console.log('Success')
        }
    
    return (
        <Fragment>
            <img className="Group7" src={Login1} alt=""/>
            <h1 className="large text-primary test">Welcome To Muzo</h1>
            <h1 className="Continue">Continue with</h1>
            <Input className="Group24" type="email" placeholder="       Enter Email"/>
            <Input className="Group23" type="password"placeholder="       Enter Password"/>
            <Link to="/UserDetails">
                <Button className="SignUp">
                    Sign up
                </Button>
            </Link>
            <h1 className="OrUsing">Or using</h1>
            <Link to="/UserDetails">
                <Button className="Google"><img src={Google}/></Button>
                <Button className="Facebook"><img src={Facebook}/></Button>
            </Link>
        </Fragment>
    )
}
export default Login;