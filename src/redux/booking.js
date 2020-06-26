import * as ActionTypes from './ActionTypes';

export const Bookings = (state = {
    errMess: null,
    bookings: []
}, action) => {
    switch (action.type) {
        case ActionTypes.ADD_BOOKINGS:
            return{...state, isLoading: false, errMess: null, bookings: action.payload};
        case ActionTypes.BOOKINGS_FAILED:
            return{...state, isLoading: false, errMess: action.payload, bookings: []};

        case ActionTypes.ADD_BOOKING:
            var booking = action.payload;
            console.log("Booking: ", booking);
            return {...state, bookings: state.bookings.concat(booking)};

        default:
          return state;
      }
};