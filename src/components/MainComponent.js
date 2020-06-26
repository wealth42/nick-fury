import React, { Component } from 'react';
import Book from './bookComponents';
import Home from './HomeComponent';
import About from './AboutComponent';
import Contact from './ContactComponent';
import Bookings from './showBookingComponent';
import TherapistDetailComponent from './therapistDetailComponent';
import { connect } from 'react-redux';
import Header from './HeaderComponent';
import Footer from './FooterComponent'
import { Switch, Route, Redirect, withRouter } from 'react-router-dom';
import { postComment, fetchTherapists, fetchComments, fetchPromos, fetchLeaders, postFeedback, postBooking,
        postTherapist, postUser, fetchBookings } from '../redux/ActionCreators';
import {actions} from 'react-redux-form';
import { TransitionGroup, CSSTransition } from 'react-transition-group';


 const mapStateToProps = state => {
   return {
      therapists: state.therapists,
      comments: state.comments,
      promotions: state.promotions,
      leaders: state.leaders,
      bookings: state.bookings,
    };  
  }

 const mapDispatchToProps = dispatch => ({
  
    postComment: (therapistId, rating, author, comment) => dispatch(postComment(therapistId, rating, author, comment)),
    fetchTherapists: () => {dispatch(fetchTherapists())},
    fetchComments: () => {dispatch(fetchComments())},
    fetchPromos: () => {dispatch(fetchPromos())},
    fetchLeaders: () => {dispatch(fetchLeaders())},
    fetchBookings: () => {dispatch(fetchBookings())},
    postFeedback: (firstname, lastname, telnum, email, agree, contactTpye, message) => 
         dispatch(postFeedback(firstname, lastname, telnum, email, agree, contactTpye, message)),
    postBooking: (therapistId, firstname, lastname, telnum, email, bookingSlot, message) =>
        dispatch(postBooking(therapistId, firstname, lastname, telnum, email, bookingSlot, message)),
    postTherapist: (name, email, telnum, password) =>
        dispatch(postTherapist(name, email, telnum, password)),
    postUser: (name, email, telnum, password) =>
        dispatch(postUser(name, email, telnum, password)),
    resetFeedbackForm: () => { dispatch(actions.reset('feedback'))},
    resetBookingForm: () => { dispatch(actions.reset('booking'))},
    resetRegisterForm: () => {dispatch(actions.reset('therapist', 'user'))}
  });


class Main extends Component {

  constructor(props) {
    super(props);
    this.state = {
        
        // selectedDish: null
    };
  }

  componentDidMount() {
    this.props.fetchTherapists();
    this.props.fetchComments();
    this.props.fetchPromos();
    this.props.fetchLeaders();
    this.props.fetchBookings();
  }


  // onDishSelect(dishId) {
  //   this.setprops({ selectedDish: dishId});
  // }
  // renderDish(dish) {
  //       if (dish != null)
  //           return(
  //               <DishDetailComponent dish={dish}></DishDetailComponent>
  //           );
  //       else
  //           return(
  //               <div></div>
  //           );
  //   }

  

  render() {
    const HomePage = () => {
    return(
        <Home therapist={this.props.therapists.therapists.filter((therapist) => therapist.featured)[0]}
              therapistsLoading = {this.props.therapists.isLoading} therapistsErrMess = {this.props.therapists.errMess}
            promotion={this.props.promotions.promotions.filter((promotion) => promotion.featured)[0]}
            promosLoading = {this.props.promotions.isLoading} promosErrMess = {this.props.promotions.errMess}
            leader={this.props.leaders.leaders.filter((leader) => leader.featured)[0]}
            leadersLoading = {this.props.leaders.isLoading} leadersErrMess = {this.props.leaders.errMess}
            
         /> //ask anyone why we used this [0] here
      );
    }

    const TherapistWithId = ({match}) =>{
      return (
       <TherapistDetailComponent therapist={this.props.therapists.therapists.filter((therapist) => therapist.id === parseInt(match.params.therapistId,10))[0]}
          isLoading = {this.props.therapists.isLoading} errMess = {this.props.therapists.errMess}
        comments={this.props.comments.comments.filter((comment) => comment.therapistId === parseInt(match.params.therapistId,10))}
        commentsErrMess = {this.props.comments.errMess}
          postComment={this.props.postComment}
          postBooking={this.props.postBooking} resetBookingForm={this.props.resetBookingForm}
      />
        );
    };

    return (
      <div>
        <Header postTherapist={this.props.postTherapist}
          postUser={this.props.postUser} resetRegisterForm={this.props.resetRegisterForm} />
        <TransitionGroup>
          <CSSTransition key={this.props.location.key} classNames="page" timeout={300} >
            <Switch>
              <Route path="/home" component={HomePage} />
              <Route exact path="/book" component={() => <Book therapists={this.props.therapists} /> } />
              <Route exact path="/aboutus" component={() => <About leaders={this.props.leaders} /> } />
              <Route path="/book/:therapistId" component={TherapistWithId} />
              <Route path="/bookings" component={() => <Bookings bookings={this.props.bookings} /> } />
              <Route exact path="/contactus" component={() => <Contact 
                  postFeedback={this.props.postFeedback} resetFeedbackForm={this.props.resetFeedbackForm} /> } />
              <Redirect to="/home" />
            </Switch> 
          {/*<Menu dishes={this.props.dishes} onClick={(dishId) => this.onDishSelect(dishId)} />
          <div className="container">
          {this.renderDish(this.props.dishes.filter((dish) => dish.id === this.props.selectedDish)[0])}
          </div>*/}
          </CSSTransition>
        </TransitionGroup>
        <Footer />
      </div>
    );
  }
}

export default withRouter(connect(mapStateToProps, mapDispatchToProps)(Main));