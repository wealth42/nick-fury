import * as ActionTypes from './ActionTypes';

export const Therapists = (state = {
	isLoading: true,
	errMess: null,
	therapists: []
	}, action) => {
    switch (action.type) {
    	case ActionTypes.ADD_THERAPISTS:
    		return{...state, isLoading: false, errMess: null, therapists: action.payload};


    	case ActionTypes.THERAPISTS_LOADING:
    		return{...state, isLoading: true, errMess: null, therapists: []};

    	case ActionTypes.THERAPISTS_FAILED:
    		return{...state, isLoading: false, errMess: action.payload, therapists: []};

        default:
          return state;
      }
};