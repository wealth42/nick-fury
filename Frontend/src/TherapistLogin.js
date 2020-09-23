import React, { Component, useState } from 'react';
import axios from 'axios';
import { setUserSession } from './Utils/Common';
import { Button, FormGroup, Form, Input, Label } from "reactstrap";

function TherapistLogin(props) {
    const [loading, setLoading] = useState(false);
    const username = useFormInput('');
    const password = useFormInput('');
    const [error, setError] = useState(null);

    // handle button click of login form
    const handleLogin = () => {
        setError(null);
        setLoading(true);
        axios.post('http://localhost:4000/users/signin', { username: username.value, password: password.value }).then(response => {
            setLoading(false);
            setUserSession(response.data.token, response.data.user);
            props.history.push('/therapistdashboard');
        }).catch(error => {
            setLoading(false);
            if (error.response.status === 401) setError(error.response.data.message);
            else setError("Something went wrong. Please try again later.");
        });
    }
    return (
        <div className="container">
            <div className="row">
                <div className="Login col-12 col-md">
                    <div className="col-12 col-md center pb-5">
                        <h3>THERAPIST LOGIN</h3>
                    </div>
                    <Form>
                        <FormGroup>
                            <Label htmlFor="username">Username</Label>
                            <Input
                                id="username" type="text" {...username} autoComplete="new-password"
                            />
                        </FormGroup>
                        <FormGroup>
                            <Label htmlFor="password">Password</Label>
                            <Input
                                type="password" id="password" {...password} autoComplete="new-password"
                            />
                        </FormGroup>
                        <FormGroup check>
                            <Label check>
                                <Input type="checkbox" name="remember" />
                          Remember me
                      </Label>
                        </FormGroup>
                        {error && <><small style={{ color: 'red' }}>{error}</small><br /></>}<br />
                        <Button type="submit" value={loading ? 'Loading...' : 'Login'} color="primary" onClick={handleLogin} disabled={loading} >
                            Login
                      </Button>
                    </Form>
                </div>
            </div>
        </div>
    );
}
const useFormInput = initialValue => {
    const [value, setValue] = useState(initialValue);

    const handleChange = e => {
        setValue(e.target.value);
    }
    return {
        value,
        onChange: handleChange
    }
}


export default TherapistLogin;