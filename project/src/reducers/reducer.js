import * as types from "../config/type";

const INITIAL_STATE = {
  username: "",
  password: "",
  userType: "",
  medID: "",
};

export default (state = INITIAL_STATE, action) => {
  switch (action.type) {
    case types.SAVE_LOGIN_DETAILS:
      return {
        ...state,
        username: action.username,
        password: action.password,
        userType: action.userType,
        medID: action.medID,
      };

    default:
      return state;
  }
};
