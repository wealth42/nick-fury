import React, { Component } from 'react';
import { getUser, removeUserSession } from './Utils/Common';
import { ListGroup, ListGroupItem, Button, Card, CardTitle, CardText } from "reactstrap";

function Assigned(){
  return(
      <div className="col-sm-4">
          <h3>Current Therapist</h3>
          <Card body inverse color="primary">
              <CardTitle>Thera Name</CardTitle>
              <CardText>With supporting text below as a natural lead-in to additional content.</CardText>
              <Button color="warning">Start</Button>
              <Button color="secondary" className="float-right">Remove</Button>
          </Card>
      </div>
  );
}


function Dashboard(props) {
  const user = getUser();

  // handle click event of logout button
  const handleLogout = () => {
    removeUserSession();
    props.history.push('/login');
  }

  return (
    <div className = "container">
      <div>
        <Assigned/>
        <div>
          <input type="button" onClick={handleLogout} value="Logout" />
        </div>
      </div>
    </div>
  );
}

export default Dashboard;
