import React from 'react';
import { Breadcrumb, BreadcrumbItem, Card, CardBody, CardHeader, Media } from 'reactstrap';
import { Link } from 'react-router-dom';
import 'font-awesome/css/font-awesome.min.css';
import 'bootstrap-social/bootstrap-social.css';
import {Loading } from './LoadingComponent';
import { baseUrl } from '../shared/baseUrl';
import {Fade, Stagger } from 'react-animation-components';

function RenderLeader(props)
{
    console.log("RenderLeader is called");
    return (
        <Media>
            <Media left middle>
                <Media object src={baseUrl + props.leader.image} alt={props.leader.name} />
            </Media>
            <Media body className="ml-5 mb-5">
                <Media heading>{props.leader.name}</Media>
                <p>{props.leader.designation}</p>
                <p>{props.leader.description}</p>
            </Media>
        </Media>
        );
}

function About(props) {

    let leaders = "";
  if (props.leaders.isLoading) {
    leaders = (
      <div className="container">
        <div className="row">
          <Loading />
        </div>
      </div>
    );
  } else if (props.leaders.errMess) {
    leaders = (
      <div className="container">
        <div className="row">
          <h4>{props.errMess}</h4>
        </div>
      </div>
    );
  } else if (props.leaders.leaders) {
    leaders = props.leaders.leaders.map((leader, i) => {
      return (
        <Stagger in>
        <Fade in>
          <li className="list-unstyled">
            <RenderLeader key={i} leader={leader}></RenderLeader>
          </li>
        </Fade>
        </Stagger>
      );
    });
    }

    return(
        <div className="container">
            <div className="row">
                <Breadcrumb>
                    <BreadcrumbItem><Link to="/home">Home</Link></BreadcrumbItem>
                    <BreadcrumbItem active>About Us</BreadcrumbItem>
                </Breadcrumb>
                <div className="col-12">
                    <h3>About Us</h3>
                    <hr />
                </div>                
            </div>
            <div className="row row-content">
                <div className="col-12 col-md-6">
                    <h2>Our History</h2>
                    <p>Lorem ipsum sed dolore dolor velit tempor sit non in deserunt ullamco ut anim cillum officia ex fugiat eiusmod. In et ex velit sint sit commodo laboris ut.</p>
                    <p>Incididunt enim mollit commodo mollit elit sit voluptate ad enim occaecat voluptate <em>The Frying Pan</em>, Voluptate culpa exercitation ad elit in dolor esse excepteur tempor exercitation officia deserunt mollit sed occaecat incididunt.</p>
                </div>
                <div className="col-12 col-md-5">
                    <Card>
                        <CardHeader className="bg-primary text-white">Facts At a Glance</CardHeader>
                        <CardBody>
                            <dl className="row p-1">
                                <dt className="col-6">Started</dt>
                                <dd className="col-6">3 Feb. 2013</dd>
                                <dt className="col-6">Major Stake Holder</dt>
                                <dd className="col-6">HK Fine Inc.</dd>
                                <dt className="col-6">Last Year's Turnover</dt>
                                <dd className="col-6">$1,250,375</dd>
                                <dt className="col-6">Employees</dt>
                                <dd className="col-6">40</dd>
                            </dl>
                        </CardBody>
                    </Card>
                </div>
                <div className="col-12">
                    <Card>
                        <CardBody className="bg-faded">
                            <blockquote className="blockquote">
                                <p className="mb-0">You better cut the pizza in four pieces because
                                    I'm not hungry enough to eat six.</p>
                                <footer className="blockquote-footer">Yogi Berra,
                                <cite title="Source Title">The Wit and Wisdom of Yogi Berra,
                                    P. Pepe, Diversion Books, 2014</cite>
                                </footer>
                            </blockquote>
                        </CardBody>
                    </Card>
                </div>
            </div>
            <div className="row row-content">
                <div className="col-12">
                    <h2>Corporate Leadership</h2>
                </div>
                <div className="col-12">
                    <Media list className="m-2">
                        {leaders}
                    </Media>
                </div>
            </div>
        </div>
    );
}

export default About;    