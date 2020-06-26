import * as ActionTypes from './ActionTypes';
import { baseUrl } from '../shared/baseUrl';


export const addComment = (comment) => ({
    type: ActionTypes.ADD_COMMENT,
    payload: comment
});

export const postComment = (therapistId, rating, author, comment) => (dispatch) => {

    const newComment = {
        therapistId: therapistId,
        rating: rating,
        author: author,
        comment: comment
    };
    newComment.date = new Date().toISOString();
    
    return fetch(baseUrl + 'comments', {
        method: "POST",
        body: JSON.stringify(newComment),
        headers: {
          "Content-Type": "application/json"
        },
        credentials: "same-origin"
    })
    .then(response => {
        if (response.ok) {
          return response;
        } else {
          var error = new Error('Error ' + response.status + ': ' + response.statusText);
          error.response = response;
          throw error;
        }
      },
      error => {
            throw error;
      })
    .then(response => response.json())
    .then(response => dispatch(addComment(response)))
    .catch(error =>  { console.log('post comments', error.message); 
    	alert('Your comment could not be posted\nError: '+error.message); });
};

export const postTherapist = (name, email, telnum, password, image, featured, description) => (dispatch) => {

    const newTherapist = {
        name: name,
        email: email,
        telnum: telnum,
        password: password,
        image: 'images/therapy.jpeg',
        featured: false,
        description: 'Nostrud velit ex sit esse in aliquip duis laborum eu nostrud voluptate dolore.'
    };
    
    return fetch(baseUrl + 'therapists', {
        method: "POST",
        body: JSON.stringify(newTherapist),
        headers: {
          "Content-Type": "application/json"
        },
        credentials: "same-origin"
    })
    .then(response => {
        if (response.ok) {
          return response;
        } else {
          var error = new Error('Error ' + response.status + ': ' + response.statusText);
          error.response = response;
          throw error;
        }
      },
      error => {
            throw error;
      })
    .then(response => response.json())
    .then(response => dispatch(addTherapist(response)))
    .catch(error =>  { console.log('post Therapist:', error.message); 
        alert('Therapist could not be registered\nError: '+error.message); });
};
export const addTherapist = (therapist) => ({
    type: ActionTypes.ADD_THERAPIST,
    payload:  therapist
});

export const postUser = (name, email, telnum, password) => (dispatch) => {

    const newUser = {
        name: name,
        email: email,
        telnum: telnum,
        password: password
    };
    
    return fetch(baseUrl + 'users', {
        method: "POST",
        body: JSON.stringify(newUser),
        headers: {
          "Content-Type": "application/json"
        },
        credentials: "same-origin"
    })
    .then(response => {
        if (response.ok) {
          return response;
        } else {
          var error = new Error('Error ' + response.status + ': ' + response.statusText);
          error.response = response;
          throw error;
        }
      },
      error => {
            throw error;
      })
    .then(response => response.json())
    .then(response => dispatch(addUser(response)))
    .catch(error =>  { console.log('post User:', error.message); 
        alert('User could not be registered\nError: '+error.message); });
};
export const addUser = (user) => ({
    type: ActionTypes.ADD_USER,
    payload:  user
});



export const postFeedback = ( firstname, lastname, telnum, email, agree, contactType,message ) => 
                            (dispatch) => {
	const newFeedback = {
        firstname: firstname,
        lastname: lastname,
        telnum: telnum,
        email: email,
        agree: agree,
        contactType: contactType,
        message: message
    };
    newFeedback.date = new Date().toISOString();
    return fetch(baseUrl + 'feedback', {
    	method: "POST",
        body: JSON.stringify(newFeedback),
        headers: {
          "Content-Type": "application/json"
        },
        credentials: "same-origin"
    })
    .then(response => {
        if (response.ok) {
          return response;
        } else {
          var error = new Error('Error ' + response.status + ': ' + response.statusText);
          error.response = response;
          throw error;
        }
      },
      error => {
            throw error;
      })
    .then(response => response.json())
    .then(response => {
    	const responseString = JSON.stringify(response);
    	alert("Thank you for your feedback\n"+responseString);
    })
    .catch(error =>{
    	console.log("post Feedback Error: "+error.message);
    	alert("Your feedback could not be posted\nError: "+error.message);
    });
};

export const postBooking = ( therapistId, firstname, lastname, telnum, email, bookingSlot, message ) => 
                            (dispatch) => {
    const newBooking = {
        therapistId: therapistId,
        firstname: firstname,
        lastname: lastname,
        telnum: telnum,
        email: email,
        bookingSlot: bookingSlot,
        message: message
    };
    newBooking.date = new Date().toISOString();
    
    return fetch(baseUrl + 'bookings', {
        method: "POST",
        body: JSON.stringify(newBooking),
        headers: {
          "Content-Type": "application/json"
        },
        credentials: "same-origin"
    })
    .then(response => {
        if (response.ok) {
          return response;
        } else {
          var error = new Error('Error ' + response.status + ': ' + response.statusText);
          error.response = response;
          throw error;
        }
      },
      error => {
            throw error;
      })
    .then(response => response.json())
    .then(response => dispatch(addBooking(response)))
    .catch(error =>  { console.log('post bookings', error.message); 
        alert('Your Booking could not be made\nError: '+error.message); });
};
export const addBooking = (bookings) => ({
    type: ActionTypes.ADD_BOOKING,
    payload: bookings
});
export const fetchBookings = () => (dispatch) => {    
    return fetch(baseUrl + 'bookings')
        .then(response => {
            if(response.ok)
                return response;
            else
            {
                var error = new Error('Error '+response.status+': '+response.statusText);
                error.response = response;
                throw error;
            }
        }, error => {
            var errmess = new Error(error.message);
            throw errmess;
            })
    .then(response => response.json())
    .then(bookings => dispatch(addBookings(bookings)))
    .catch(error => dispatch(bookingsFailed(error.message)));

};

export const bookingsFailed = (errmess) => ({
    type: ActionTypes.BOOKINGS_FAILED,
    payload: errmess
});

export const addBookings = (bookings) => ({
    type: ActionTypes.ADD_BOOKINGS,
    payload: bookings
});


export const fetchTherapists = () => (dispatch) => {
	dispatch(therapistsLoading(true));

	return fetch(baseUrl + 'therapists')
		.then(response => {
			if(response.ok)
				return response;
			else
			{
				var error = new Error('Error '+response.status+': '+response.statusText);
				error.response = response;
				throw error;
			}
		}, error => {
			var errmess = new Error(error.message);
			throw errmess;
			})
		.then(response => response.json())
		.then(therapists => dispatch(addTherapists(therapists)))
		.catch(error => dispatch(therapistsFailed(error.message)));
}

export const therapistsLoading = () =>({
	type: ActionTypes.THERAPISTS_LOADING 
});
export const therapistsFailed = (errmess) => ({
	type: ActionTypes.THERAPISTS_FAILED,
	payload: errmess
});
export const addTherapists = (therapists) => ({
	type: ActionTypes.ADD_THERAPISTS,
	payload: therapists
});


export const fetchComments = () => (dispatch) => {    
    return fetch(baseUrl + 'comments')
		.then(response => {
			if(response.ok)
				return response;
			else
			{
				var error = new Error('Error '+response.status+': '+response.statusText);
				error.response = response;
				throw error;
			}
		}, error => {
			var errmess = new Error(error.message);
			throw errmess;
			})
    .then(response => response.json())
    .then(comments => dispatch(addComments(comments)))
	.catch(error => dispatch(commentsFailed(error.message)));

};

export const commentsFailed = (errmess) => ({
    type: ActionTypes.COMMENTS_FAILED,
    payload: errmess
});

export const addComments = (comments) => ({
    type: ActionTypes.ADD_COMMENTS,
    payload: comments
});

export const fetchPromos = () => (dispatch) => {
    
    dispatch(promosLoading());

    return fetch(baseUrl + 'promotions')
		.then(response => {
			if(response.ok)
				return response;
			else
			{
				var error = new Error('Error '+response.status+': '+response.statusText);
				error.response = response;
				throw error;
			}
		}, error => {
			var errmess = new Error(error.message);
			throw errmess;
			})
    .then(response => response.json())
    .then(promos => dispatch(addPromos(promos)))
	.catch(error => dispatch(promosFailed(error.message)));

}

export const promosLoading = () => ({
    type: ActionTypes.PROMOS_LOADING
});

export const promosFailed = (errmess) => ({
    type: ActionTypes.PROMOS_FAILED,
    payload: errmess
});

export const addPromos = (promos) => ({
    type: ActionTypes.ADD_PROMOS,
    payload: promos
});

export const fetchLeaders = () => (dispatch) => {
    
    dispatch(leadersLoading());

    return fetch(baseUrl + 'leaders')
		.then(response => {
			if(response.ok)
				return response;
			else
			{
				var error = new Error('Error '+response.status+': '+response.statusText);
				error.response = response;
				throw error;
			}
		}, error => {
			var errmess = new Error(error.message);
			throw errmess;
			})
    .then(response => response.json())
    .then(leaders => dispatch(addLeaders(leaders)))
	.catch(error => dispatch(leadersFailed(error.message)));

}

export const leadersLoading = () => ({
    type: ActionTypes.LEADERS_LOADING
});

export const leadersFailed = (errmess) => ({
    type: ActionTypes.LEADERS_FAILED,
    payload: errmess
});

export const addLeaders = (leaders) => ({
    type: ActionTypes.ADD_LEADERS,
    payload: leaders
});
 