import React from "react";
import ReactDom from "react-dom";
import { BrowserRouter, Switch, Route } from "react-router-dom";
import PrivateRoute from './Utils/PrivateRoute';
import PublicRoute from './Utils/PublicRoute';
import { getToken, removeUserSession, setUserSession } from './Utils/Common';

import Home from "./Home";
import ClientLogin from "./ClientLogin";
import ClientDashboard from "./ClientDashboard";
import TherapistLogin from "./TherapistLogin";
import TherapistDashboard from "./TherapistDashboard";

function Main(props) {
    return (
        <div>
            <BrowserRouter>
                <Switch>
                    <Route exact path="/" component={Home} />
                    <PublicRoute exact path="/clientlogin" component={ClientLogin}/>
                    <PublicRoute exact path="/therapistlogin" component={TherapistLogin}/>
                    <PrivateRoute exact path="/clientdashboard" component={ClientDashboard}/>
                    <Route exact path="/therapistdashboard" component={TherapistDashboard}/>
                </Switch>
            </BrowserRouter>
        </div>

    );
}

export default Main;
