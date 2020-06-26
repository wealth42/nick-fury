import {createStore, combineReducers, applyMiddleware} from 'redux';
import { Therapists } from './therapists';
import { Comments } from './comments';
import { Promotions } from './promotions';
import { Leaders } from './leaders';
import { Bookings } from './booking';
import thunk from 'redux-thunk';
import logger from 'redux-logger';
import {createForms} from 'react-redux-form';
import {InitialFeedback, InitialBooking} from './forms'

export const ConfigureStore = () => {
    const store = createStore(
        combineReducers({
            therapists: Therapists,
            comments: Comments,
            promotions: Promotions,
            leaders: Leaders,
            bookings: Bookings,

            ...createForms({
            	feedback: InitialFeedback,
                booking: InitialBooking
            })
        }),
        applyMiddleware(thunk, logger)
    );

    return store;
}