import React from 'react';
import { Breadcrumb, BreadcrumbItem, Card, CardBody, CardHeader, Media } from 'reactstrap';
import { Link } from 'react-router-dom';
import 'font-awesome/css/font-awesome.min.css';
import 'bootstrap-social/bootstrap-social.css';
import {Loading } from './LoadingComponent';
import { baseUrl } from '../shared/baseUrl';
import {Fade, Stagger } from 'react-animation-components';

function RenderBooking(props)
{
    console.log("RenderBooking is called");
    return (
        <Media>
            <Media body className="ml-5 mb-5">
                <Media heading>{props.booking.firstname} {props.booking.lastname}</Media>
                <p>Booking Slot: {props.booking.bookingSlot}</p>
                <p>Instruction: {props.booking.message}</p>
                <p>Contact No: {props.booking.telnum}</p>
                <p>Therapist Id: {props.booking.therapistId}</p>
            </Media>
        </Media>
        );
}

function Bookings(props) {
    console.log(props);
    var bookings = "";
  
   if (props.bookings.errMess) {
    bookings = (
      <div className="container">
        <div className="row">
          <h4>{props.errMess}</h4>
        </div>
      </div>
    );
  } else if (props.bookings.bookings) {
    bookings = props.bookings.bookings.map((booking, i) => {
      return (
        <Stagger in>
        <Fade in>
          <li className="list-unstyled">
            <RenderBooking key={i} booking={booking}></RenderBooking>
          </li>
        </Fade>
        </Stagger>
      );
    });
    }

    return(
        <div className="container">
            <div className="row">
                <Breadcrumb>
                    <BreadcrumbItem><Link to="/home">Home</Link></BreadcrumbItem>
                    <BreadcrumbItem active>All Bookings:</BreadcrumbItem>
                </Breadcrumb>
                <div className="col-12">
                    <hr />
                </div>                
            </div>
            <div className="row row-content">
                <div className="col-12">
                    <Media list className="m-2">
                        {bookings}
                    </Media>
                </div>
            </div>
        </div>
    );
}

export default Bookings;  