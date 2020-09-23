import React from 'react';
import { getUser, removeUserSession } from './Utils/Common';
import { Button, Card, CardTitle, CardText, CardHeader, ListGroup, ListGroupItem } from "reactstrap";

function Assigned() {
    return (
        <div className="row">
            <div className="col-sm-6">
                <Card body inverse color="primary" style={{ width: '20rem' }}>
                    <CardHeader>Therapist Assigned</CardHeader>
                    <CardTitle>Therapist 1</CardTitle>
                    <CardText>With supporting text below as a natural lead-in to additional content.<small>(Therapist Desc.)</small></CardText>
                    <Button color="warning">Start</Button>
                    <Button color="secondary" className="float-right">Remove</Button>
                </Card>
            </div>
            <div className="col-sm-6">
                <Card style={{ width: '20rem' }}>
                    <CardHeader>Requests</CardHeader>
                    <ListGroup variant="flush">
                        <ListGroupItem>Therapist 1<Button className="float-right">Reject</Button><Button className="float-right" color="primary">Accept</Button></ListGroupItem>
                        <ListGroupItem>Therapist 2<Button className="float-right">Reject</Button><Button className="float-right" color="primary">Accept</Button></ListGroupItem>
                        <ListGroupItem>Therapist 3<Button className="float-right">Reject</Button><Button className="float-right" color="primary">Accept</Button></ListGroupItem>
                    </ListGroup>
                </Card>
            </div>
        </div>
    );
}


function ClientDashboard(props) {
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

export default ClientDashboard;
