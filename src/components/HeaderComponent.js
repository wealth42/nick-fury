import React, {Component} from 'react';
import { Navbar, NavbarBrand, Nav, NavbarToggler, Collapse, NavItem, Jumbotron, Button, Modal, ModalHeader,
         Form, FormGroup, Col, Row, Label, Input, ModalBody } from 'reactstrap';
import 'font-awesome/css/font-awesome.min.css';
import 'bootstrap-social/bootstrap-social.css';
import { NavLink } from 'react-router-dom';
import { baseUrl } from '../shared/baseUrl' 
import { Control, LocalForm, Errors, action } from 'react-redux-form';


/*var loginStatus = 1;
function ReturnNavbar(props){
        console.log("I was called");
        if(loginStatus == 0)
        return(
            <Nav className="ml-auto" navbar>
                        <NavItem>
                            <Button outline onClick={props.toggleModal}>
                                <span className="fa fa-sign-in fa-lg">Login</span>
                            </Button>
                        </NavItem>
            </Nav>
            );
    else if(loginStatus == 1)
        return(
                <Nav className="ml-auto" navbar>
                        <NavItem>
                            <NavLink className="nav-link" to="/book">
                                <span className="fa fa-list fa-lg"> </span> Book Therapist
                            </NavLink>
                        </NavItem>
                        <NavItem>
                            <Button outline onClick={props.handleLogout}>
                                <span className="fa fa-sign-out fa-lg">Logout</span>
                            </Button>
                        </NavItem>
                </Nav>
            );
    else if(loginStatus == 2)
        return(
                <Nav className="ml-auto" navbar>
                        <NavItem>
                            <NavLink className="nav-link" to="/book">
                                <span className="fa fa-list fa-lg"> </span> Show Bookings
                            </NavLink>
                        </NavItem>
                        <NavItem>
                            <Button outline onClick={props.handleLogout}>
                                <span className="fa fa-sign-out fa-lg">Logout</span>
                            </Button>
                        </NavItem>
                </Nav>
            );
    }
*/
class Header extends Component {
    constructor(props)
    {
        super(props);
        this.state = {
            isNavOpen: false,
            isModalOpen: false,
        };
        this.toggleNav = this.toggleNav.bind(this);
        this.toggleModal = this.toggleModal.bind(this);
        this.handleLogin = this.handleLogin.bind(this);
        //this.handleLogout = this.handleLogout.bind(this);
        //this.validatelogin = this.validatelogin.bind(this);
    }

    toggleNav()
    {
        this.setState({
            isNavOpen: !this.state.isNavOpen
        });
    }
    toggleModal()
    {
        this.setState({
            isModalOpen: !this.state.isModalOpen
        });
    }
    handleLogin(event)
    {
        this.toggleModal();
        //this.validatelogin(this.username.value, this.password.value);
        alert("Username "+this.username.value+" Password: "+this.password.value+" Remember: "+this.remember.checked);
        event.preventDefault();
    }
   /* handleLogout()
    {
        this.toggleModal();
        loginStatus = 0;
    }
    validatelogin(username, password)
    {
        //const checkUser = (username, password) => {
            if((baseUrl+'users?email='+username) != '' && (baseUrl+'users?password='+password) != '' )
                loginStatus = 1;
            else if( (baseUrl+'therapists?email='+username) != '' && (baseUrl+'therapists?password='+password) != '' )
                loginStatus = 2;
            else
                alert("username or password was not correct");
            if((baseUrl+'users?email='+username) == true)
                alert("yes");
            else
                alert("no");
    }*/


	render() {
		return(
			<>
			<Navbar dark expand="md">
          		<div className="container">
                <NavbarToggler onClick={this.toggleNav} />
            		<NavbarBrand className="mr-auto" href="/">
                        <img src={baseUrl + "images/logo.svg"} height="30" width="41"
                            alt="Wealth 42" />
                    </NavbarBrand>
                    <Collapse isOpen={this.state.isNavOpen} navbar>
                    <Nav navbar>
                        <NavItem>
                            <NavLink className="nav-link" to="/home">
                                <span className="fa fa-home fa-lg"> </span> Home
                            </NavLink>
                        </NavItem>
                        <NavItem>
                            <NavLink className="nav-link" to="/aboutus">
                                <span className="fa fa-info fa-lg"> </span> About us
                            </NavLink>
                        </NavItem>
                        <NavItem>
                            <NavLink className="nav-link" to="/contactus">
                                <span className="fa fa-address-card fa-lg"> </span> Contact us
                            </NavLink>
                        </NavItem>
                        </Nav>
                    <Nav className="ml-auto" navbar>
                        <NavItem>
                            <NavLink className="nav-link" to="/book">
                                <span className="fa fa-list fa-lg"> </span> Book Therapist
                            </NavLink>
                        </NavItem>
                        <NavItem>
                            <NavLink className="nav-link" to="/bookings">
                                <span className="fa fa-list fa-lg"> </span> Show Bookings
                            </NavLink>
                        </NavItem>
                        <NavItem>
                            <Button outline onClick={this.toggleModal}>
                                <span className="fa fa-sign-in fa-lg">Login</span>
                            </Button>
                        </NavItem>
                    </Nav>
                    </Collapse>
          		</div>
        	</Navbar>
        	<Jumbotron>
        		<div className="container">
        			<div className="row row-header">
        				<div className="col-12 col-sm-6">
        					<h1>Wealth 42</h1>
        					<p>Officia sunt dolore ea duis amet commodo veni
                            am ea velit aliquip ullamco pariatur do incididunt do ullamco velit.
                            Lorem ipsum aliqua consequat sit do incididunt proident in velit enim ullamco minim.</p>
        				</div>
        			</div>
        		</div>
        	</Jumbotron>
            <Modal isOpen={this.state.isModalOpen} toggle={this.toggleModal}>
                <ModalHeader toggle={this.toggleModal}>
                    Login
                </ModalHeader>
                <ModalBody>
                    <Form onSubmit={this.handleLogin}>
                        <FormGroup>
                            <Label htmlFor="username">Username</Label>
                            <Input type="text" id="username" name="username" placeholder="Username"
                                innerRef={(input) => this.username = input}/>
                        </FormGroup>
                        <FormGroup>
                            <Label htmlFor="Password">Password</Label>
                            <Input type="password" id="password" name="password" placeholder="Password"
                                innerRef={(input) => this.password = input}/>
                        </FormGroup>
                        <FormGroup check>
                            <Label check>
                                <Input type="checkbox" name="remember" 
                                    innerRef={(input) => this.remember = input}/>
                                Remember me
                            </Label>
                        </FormGroup>
                        <Button type="submit" value="submit" color="primary">Login</Button>
                        <RegisterForm postTherapist={this.props.postTherapist} postUser={this.props.postUser}
                            resetRegisterForm={this.props.resetRegisterForm}/>
                    </Form>
                </ModalBody>
            </Modal>
    	</>
			);
	}
}

const required = (val) => val && val.length;
const maxLength = (len) => (val) => !(val) || (val.length <= len);
const minLength = (len) => (val) => val && (val.length >= len);
const isNumber = (val) => !isNaN(Number(val));
const validEmail = (val) => /^[A-z0-9._%+-]+@[A-z0-9.-]+\.[A-Z]{2,4}$/i.test(val);

 class RegisterForm extends Component{
    constructor(props){
      super(props);
      this.state = {
        isModal2Open: false,
      }
      this.toggleModal2 = this.toggleModal2.bind(this);
    }
    
    toggleModal2()
    {
        this.setState({
            isModal2Open: !this.state.isModal2Open
        });
    }
    submitValues(values)
    {
      this.toggleModal2();
      console.log("Current state is: "+JSON.stringify(values));
      //alert("Current state is: "+JSON.stringify(values));
      if(values.agree === true)
        this.props.postTherapist(values.name, values.email, values.telnum, values.password);
      else
        this.props.postUser(values.name, values.email, values.telnum, values.password);
    this.props.resetRegisterForm();
    }

    render()
    {
      return(
          <>
            <Button className="btn btn-success border-dark" onClick={this.toggleModal2} >
              &nbsp; Sign Up Now
            </Button>
            <Modal isOpen={this.state.isModal2Open} toggle={this.toggleModal2}>
              <ModalHeader toggle={this.toggleModal2}>Registration details</ModalHeader>
              <ModalBody>
                <LocalForm onSubmit={values => {this.submitValues(values)}}>
                  <Row className="form-group">
                    <Label htmlFor="name" md={2}>Name</Label>
                    <Col md={10}>
                      <Control.text model=".name" id="name" name="name" className="form-control"
                         placeholder="Full Name" validators={{
                              required, minLength: minLength(3), maxLength: maxLength(20)}}/>
                          <Errors className="text-danger" model=".name" show="touched"
                            messages={{
                              required: "Required ", minLength: "Must be more than 2 characters",
                              maxLength: "Must be 20 characters or less"
                            }} />
                    </Col>
                    </Row>
                    <Row className="form-group">
                            <Label htmlFor="email" md={2}>Email</Label>
                            <Col md={10}>
                                <Control.text model=".email" id="email" name="email" placeholder="Email"
                                        className="form-control" 
                                        validators={{
                                            required, validEmail
                                         }}/>
                                <Errors
                                    className="text-danger" model=".email" show="touched"
                                    messages={{
                                        required: 'Required', 
                                        validEmail: 'Invalid Email address'
                                    }}
                                />
                            </Col>
                        </Row>
                         <Row className="form-group">
                            <Label htmlFor="telnum" md={3}>Contact No.</Label>
                            <Col md={9}>
                                <Control.text model=".telnum" id="telnum" name="telnum" placeholder="Contact no."
                                        className="form-control"
                                        validators={{
                                            required, minLength: minLength(6), maxLength: maxLength(10), isNumber
                                         }} />
                                <Errors
                                    className="text-danger" model=".telnum" show="touched"
                                    messages={{
                                        required: 'Required', minLength: 'Must be Greater than 6 Numbers',
                                        maxLength: 'Must be 10 Numbers or Less', isNumber: 'Must be a Number'
                                    }}
                                />
                            </Col>
                        </Row>
                        <Row className="form-group">
                            <Label htmlFor="password" md={2}>Password</Label>
                            <Col md={10}>
                                <Control type="password" model=".password" id="password" name="password" placeholder="password"
                                        className="form-control" 
                                        validators={{
                                            required
                                         }}/>
                                <Errors
                                    className="text-danger" model=".email" show="touched"
                                    messages={{
                                        required: 'Required'
                                    }}
                                />
                            </Col>
                        </Row>
                        <Row className="form-group">
                            <Col md={{size: 10, offset: 2}} >
                                <div className="form-check">
                                    <Label check>
                                        <Control.checkbox model=".agree" name="agree" 
                                            className="form-checkinput" /> {' '}
                                        <strong>Register as a Therapist?</strong>
                                    </Label>
                                </div>
                            </Col>
                        </Row>
                  <Row className="form-group">
                    <Col md={{size:10}}>
                      <Button type="submit" color="primary">
                        Sign Up
                      </Button>
                    </Col>
                  </Row>
                </LocalForm>
              </ModalBody>
            </Modal>
          </>
        );
    }
  }

export default Header;