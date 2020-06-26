import React, { Component } from 'react';
import { Card, CardImg, CardImgOverlay, CardText, CardBody, CardTitle, Breadcrumb, BreadcrumbItem,
        Modal, ModalHeader, ModalBody, Button, Row, Col, Label } from 'reactstrap';
import {Link } from 'react-router-dom';
import { Control, LocalForm, Errors, Form, action } from 'react-redux-form';
import 'font-awesome/css/font-awesome.min.css';
import { Loading } from './LoadingComponent';
import { baseUrl } from '../shared/baseUrl'  
import { FadeTransform, Fade, Stagger } from 'react-animation-components';

function RenderTherapist({therapist})
{
	return(
		<div className="col-12 col-md-5 m-1">
          <FadeTransform in transformProps={{
                              exitTransform: 'scale(0.5) translateY(-50%)'
                              }}>
            <Card>
              <CardImg width="100%" src={baseUrl + therapist.image} alt={therapist.name} />
              <CardBody>
                  <CardTitle>{therapist.name}</CardTitle>
                  <CardText>{therapist.description}</CardText>
              </CardBody>
            </Card>
          </FadeTransform>
        </div>
		);
}

	

 function RenderComments({comments, postComment, therapistId, postBooking, resetBookingForm})
 { //console.log("Render comments is called");
 	if(comments!=null)
 		return(
 			<div className="col-12 col-md-5 m-1">
        	  <h3>Comments</h3>
        	  <ul className="list-unstyled">
           <Stagger in>
        	  	{comments.map((comment) => {
        	  		return(
                  <Fade in>
           	  			<li key={comment.id}>
           				<p>{comment.comment}</p>
           				  
           				<p>-- {comment.author},  {new Intl.DateTimeFormat('en-US', {year:'numeric', month:'short',
             							 day:'2-digit'}).format(new Date(Date.parse(comment.date)))} </p>
           				  
           				</li>
                  </Fade>
        	  			);
        	  	})}
            </Stagger>
        	  </ul>
            <CommentForm therapistId={therapistId} postComment={postComment}>
            </CommentForm>
            <MakeBookings therapistId={therapistId} postBooking={postBooking} resetBookingForm={resetBookingForm} />
        	</div>
 			);
 }
 function TherapistDetailComponent(props){
    console.log("TherapistDetailComponent is called");
    if(props.isLoading) {
      return(
        <div className="container">
          <div className="row">
            <Loading />
          </div>
        </div>
        );
    }
    else if (props.errMess)
    {
      return(
        <div className="container">
          <div className="row">
            <h4>{props.errMess}</h4>
          </div>
        </div>
        );
    }
    else if(props.therapist != null)
    	return (
    		<div className="container">
      			<div className="row">
      				<Breadcrumb>
    			        <BreadcrumbItem> <Link to="/book">Book Therapist</Link></BreadcrumbItem>
            			<BreadcrumbItem active>{props.therapist.name}</BreadcrumbItem>
            		</Breadcrumb>
            		<div className="col-12">
            			<h3>{props.therapist.name}</h3>
            			<hr />
            		</div>
            	</div>
            	<div className="row">
        			<RenderTherapist therapist={props.therapist} />
        			<RenderComments comments={props.comments} 
                  postComment={props.postComment}
                  therapistId={props.therapist.id} 
                  postBooking = {props.postBooking} resetBookingForm={props.resetBookingForm}/>
      			</div>
      		</div>
    	);
    else
    	return(
    		<div> </div>
    		);
  }

  class MakeBookings extends Component{
    constructor(props){
      super(props);
      this.state={
        isModalOpen: false
      }
      this.toggleModal = this.toggleModal.bind(this);
      this.handleSubmit = this.handleSubmit.bind(this);
    }
    
    toggleModal()
    {
        this.setState({
            isModalOpen: !this.state.isModalOpen
        });
    }
    handleSubmit(values)
    {
      this.toggleModal();
        
        this.props.postBooking(
            this.props.therapistId,
            values.firstname,
            values.lastname,
            values.telnum,
            values.email,
            values.bookingSlot,
            values.message
            );
        this.props.resetBookingForm();    
    }

    render()
    {
      return(
          <>
            <Button className="btn btn-light border-dark" onClick={this.toggleModal} >
              <i className="fa fa-pencil" aria-hidden="true"></i>
              &nbsp; Make Booking
            </Button>
            <Modal isOpen={this.state.isModalOpen} toggle={this.toggleModal}>
              <ModalHeader toggle={this.toggleModal}>Submit Booking details</ModalHeader>
              <ModalBody>
                <Form model="booking" onSubmit={(values) => this.handleSubmit(values)}>
                        <Row className="form-group">
                            <Label htmlFor="firstname" md={2}>First Name</Label>
                            <Col md={10}>
                                <Control.text model=".firstname" id="firstname" name="firstname" placeholder="First name" 
                                         className="form-control" 
                                         validators={{
                                            required, minLength: minLength(3), maxLength: maxLength(15)
                                         }}/>
                                <Errors
                                    className="text-danger" model=".firstname" show="touched"
                                    messages={{
                                        required: 'Required', minLength: 'Must be Greater than 2 characters',
                                        maxLength: 'Must be 15 characters or Less'
                                    }}
                                />
                            </Col>
                        </Row>
                        <Row className="form-group">
                            <Label htmlFor="lastname" md={2}>Last Name</Label>
                            <Col md={10}>
                                <Control.text model=".lastname" id="lastname" name="lastname" placeholder="Last name"
                                        className="form-control"
                                        validators={{
                                            required, minLength: minLength(3), maxLength: maxLength(15)
                                         }}/>
                                <Errors
                                    className="text-danger" model=".lastname" show="touched"
                                    messages={{
                                        required: 'Required', minLength: 'Must be Greater than 2 characters',
                                        maxLength: 'Must be 15 characters or Less'
                                    }}
                                />
                            </Col>
                        </Row>
                        <Row className="form-group">
                            <Label htmlFor="telnum" md={2}>Contact No.</Label>
                            <Col md={10}>
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
                          <Label htmlFor="bookingSlot" md={2}>Bookin Slot</Label>
                            <Col md={{size: 3, offset: 1}} >
                                <Control.select model=".bookingSlot" name="bookingSlot" 
                                    className="form-control" >
                                    <option>8 AM</option>
                                    <option>9.30 AM</option>
                                    <option>11 AM</option>
                                    <option>2 PM</option>
                                </Control.select>
                            </Col>
                        </Row>
                        <Row className="form-group">
                            <Label htmlFor="message" md={3}>Any Instructions?</Label>
                            <Col md={10}>
                                <Control.textarea model=".message" id="message" name="message" rows="12"
                                        className="form-control" />
                            </Col>
                        </Row>
                        <Row className="form-group">
                            <Col md={{size:10, offset:3}}>
                                <Button type="submit" color="primary">
                                    Confirm Booking
                                </Button>
                            </Col>
                        </Row>
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

  class CommentForm extends Component{
    constructor(props){
      super(props);
      this.state = {
        isModalOpen: false,
      }
      this.toggleModal = this.toggleModal.bind(this);
    }
    
    toggleModal()
    {
        this.setState({
            isModalOpen: !this.state.isModalOpen
        });
    }
    submitValues(values)
    {
      this.toggleModal();
      console.log("Current state is: "+JSON.stringify(values));
      //alert("Current state is: "+JSON.stringify(values));
      this.props.postComment(this.props.therapistId, values.rating, values.author, values.comment);
    }

    render()
    {
      return(
          <>
            <Button className="btn btn-light border-dark" onClick={this.toggleModal} >
              <i className="fa fa-pencil" aria-hidden="true"></i>
              &nbsp; Submit comment
            </Button>
            <Modal isOpen={this.state.isModalOpen} toggle={this.toggleModal}>
              <ModalHeader toggle={this.toggleModal}>Submit Comment</ModalHeader>
              <ModalBody>
                <LocalForm onSubmit={values => {this.submitValues(values)}}>
                  <Row className="form-group">
                    <Label htmlFor="rating" md={12}>Rating</Label>
                    <Col md={12}>
                      <Control.select model=".rating" id="rating" name="rating" className="form-control">
                        <option value="1">1</option>
                        <option value="2">2</option>
                        <option value="3">3</option>
                        <option value="4">4</option>
                        <option value="5">5</option>
                      </Control.select>
                    </Col>
                  </Row>
                  <Row className="form-group">
                    <Label htmlFor=".author" md={12}>Your name</Label>
                    <Col md={12}>
                      <Control.text model=".author" id="author" name="author" className="form-control"
                         placeholder="YourName" validators={{
                              required, minLength: minLength(3), maxLength: maxLength(15)}}/>
                          <Errors className="text-danger" model=".author" show="touched"
                            messages={{
                              required: "Required ", minLength: "Must be more than 2 characters",
                              maxLength: "Must be 15 characters or less"
                            }} />
                    </Col>
                  </Row>
                  <Row className="form-group">
                    <Col md={12}>
                      <Control.textarea model=".comment" id="comment" name="comment" rows="6" className="form-control"/>
                    </Col>
                  </Row>
                  <Row className="form-group">
                    <Col md={{size:10}}>
                      <Button type="submit" color="primary">
                        Submit
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

export default TherapistDetailComponent;