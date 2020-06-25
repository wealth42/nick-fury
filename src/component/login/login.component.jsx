import React from 'react';
import './login.styles.scss';

import { auth } from '../../firebase/firebase.utils';

class LogIn extends React.Component {
    constructor(props) {
      super(props);
  
      this.state = {
        email: '',
        password: ''
      };
    }

    handleSubmit = async event => {
        event.preventDefault();
        const { email, password } = this.state;
        try {
        await auth.signInWithEmailAndPassword(email, password);
        this.setState({ email: '', password: '' });
        } catch (error) {
        console.log(error);
        }
      };

    handleChange = event => {
        const { value, name } = event.target;
        this.setState({ [name]: value });
    };

    render() {
        return(
            <div className="login-box">             
                <form onSubmit={this.handleSubmit} className="form"> 
                    <h2>Login</h2>
                    <span>You need to Login First to View all features</span>
                    <span>For credentials see README.md</span>
                    <input
                        name='email'
                        type='email'
                        className='textbox'
                        onChange={this.handleChange}
                        value={this.state.email}
                        placeholder='email'
                        required
                    />
                    <input
                        name='password'
                        type='password'
                        className='textbox'
                        onChange={this.handleChange}
                        value={this.state.password}
                        placeholder='password'
                        required
                    />
                    <button type='submit' className="button">Log In</button>
                </form>
            </div>
        );
    }
}

export default LogIn;