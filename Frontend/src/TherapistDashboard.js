import React, { Component } from 'react';
import { getUser, removeUserSession } from './Utils/Common';
import { CardDeck, CardFooter, Card, Button, CardTitle, CardText, CardBody } from "reactstrap";

function Assigned() {
  return (
    <div>
      <CardDeck>
        <Card>
          <CardBody>
            <CardTitle>Client 1</CardTitle>
            <CardText>
              CLient Descprition...
            </CardText>
          </CardBody>
          <Button className="float-right">Request</Button>
          <CardFooter>
            <small className="text-muted">Last updated 3 mins ago</small>
          </CardFooter>
        </Card>
        <Card>
          <CardBody>
            <CardTitle>Client 2</CardTitle>
            <CardText>CLient Descprition...
            </CardText>
          </CardBody>
          <Button className="float-right">Request</Button>
          <CardFooter>
            <small className="text-muted">Last updated 3 mins ago</small>
          </CardFooter>
        </Card>
        <Card>
          <CardBody>
            <CardTitle>Client 3</CardTitle>
            <CardText>CLient Descprition...
      </CardText>
          </CardBody>
          <Button className="float-right">Request</Button>
          <CardFooter>
            <small className="text-muted">Last updated 3 mins ago</small>
          </CardFooter>
        </Card>
      </CardDeck>
    </div>
  );
}


function Dashboard(props) {
  const user = getUser();

  // handle click event of logout button
  const handleLogout = () => {
    removeUserSession();
    props.history.push('/');
  }

  return (
    <div className="container">
      <div>
        <Assigned />
        <div>
          <input type="button" onClick={handleLogout} value="Logout" />
        </div>
      </div>
    </div>
  );
}

export default Dashboard;
