import { API } from "../../backend";

export const getUsers = () => {
    return fetch(`${API}/users`, {method: "GET"})
    .then(response => {
        return response.json();
    })
    .catch(err => console.log(err));
}