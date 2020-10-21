import * as types from "../config/type";

export const saveLoginDetails = (userType, username, password, medID) => ({
  type: types.SAVE_LOGIN_DETAILS,
  userType,
  username,
  password,
  medID,
});
