import React from 'react';
import { Link } from 'react-router-dom';

import { auth } from '../../firebase/firebase.utils';


import './header.styles.scss';

const Header = ({ currentUser }) => (
    <div className='header'>
        <Link to="/">
            <h2>Therapy Aid</h2>
        </Link>
        <div className='options'>
            <Link className='option' to='/'>
            Dashboard
            </Link>
            <Link className='option' to='/journal'>
            Journal
            </Link>
            <Link className='option' to='/session'>
            Sessions
            </Link>
            <Link className='option' to='/test'>
            Debug
            </Link>

            {
                currentUser ? 
                <div className='option' onClick={() => auth.signOut()}>SIGN OUT</div>
                :
                <Link className='option' to='/signup'>
                    Sign In
                </Link>
            }
        </div>
    </div>
);
export default Header;