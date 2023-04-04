import React, {useState} from 'react';
import { Link } from 'react-router-dom';
import { Button } from './Button';
import './Navbar.css';

function Navbar() {
  const [click, setClick] = useState(false);
  const [button, setButton] = useState(true);

  const handleClick = () => setClick(!click);
  const closeMobileMenu = () => setClick(false);

  const showButton = () => {
    if(window.innerWidth <= 960){
      setButton(false)
    }else{
      setButton(true)
    }
  };
  window.addEventListener('rize', showButton);

  return (
    <>
        < nav className= 'navbar'>
          <div className='navbar-container'>
            <Link to='/' className='navbar-logo'>
            RAMCHAT 
            </Link>
           <div className='menu-icon' onClick={handleClick}>
             <span class={click ? "" : ""} >
  
             </span>
           </div>
           <ul className={click ? 'nav-menu active': 'nav-menu'}>
             <li className='nav-item'>
               <Link
                 to='/home' 
                 className='nav-links' 
                 onClick={closeMobileMenu}>
                 Home
               </Link>
             </li>
             <li className='nav-item'>
               <Link
                 to='/chat' 
                 className='nav-links' 
                 onClick={closeMobileMenu}>
                 Chat
               </Link>
             </li>
             <li className='nav-item'>
               <Link 
                 to='/settings' 
                 className='nav-links' 
                 onClick={closeMobileMenu}>
                 Settings
               </Link>
             </li>
             <li className='nav-item'>
               <Link 
                 to='/sign-up' 
                 className='nav-links-mobile'
                 onClick={closeMobileMenu}>
                 Signup
               </Link>
             </li>
            </ul>
            {button && <Button buttonStyle='btn--outline'>SIGN UP</Button>}
          </div>
        </nav>
    </>
  );
}

export default Navbar