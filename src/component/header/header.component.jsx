import React from 'react';
import { Link } from 'react-router-dom';

import { auth } from '../../firebase/firebase.utils';


import './header.styles.scss';

const Header = ({ currentUser }) => (
    <div className='header'>
            <h2>Therapy Aid</h2>
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
            {
                currentUser ? 
                <div className='option' onClick={() => auth.signOut()}>Sign Out</div>
                :
                <Link className='option' to='/signin'>
                    Sign In
                </Link>
            }
        </div>
    </div>
);
export default Header;