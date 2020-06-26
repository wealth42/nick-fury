import React, { Component } from 'react';
import { Card, CardImg, CardImgOverlay, CardText, CardBody, CardTitle, Breadcrumb, BreadcrumbItem } from 'reactstrap';
import TherapistDetailComponent from './therapistDetailComponent';
import { Link } from 'react-router-dom';
import { Loading } from './LoadingComponent';  
import { baseUrl } from '../shared/baseUrl'  
    
	function RenderBookItem({therapist}) 
	{
		console.log("Hello form RenderBookItem");
		return(
				<Card>
					<Link to={`/book/${therapist.id}`} >
                  <CardImg width="100%" src={baseUrl + therapist.image} alt={therapist.name} />
                  <CardImgOverlay>
                      <CardTitle>{therapist.name}</CardTitle>
                  </CardImgOverlay>
                  </Link>
                </Card>
			);

	}
  const Book = (props) =>{
    	const book = props.therapists.therapists.map((therapist) => {
            return (
              <div key={therapist.id} className="col-12 col-md-5 m-1">
                	<RenderBookItem therapist={therapist} />
              </div>
            );
        });
      if(props.therapists.isLoading)
      {
        return(
          <div className="container">
            <div className="row">
              <Loading />
            </div>
          </div>
          );
      }
      else if (props.therapists.errMess)
      {
        return(
          <div className="container">
            <div className="row">
              <h4>{props.errMess}</h4>
            </div>
          </div>
          );
      }
      else
        return (
            <div className="container">
            	<div className="row">
            		<Breadcrumb>
            			<BreadcrumbItem> <Link to="/home">Home</Link></BreadcrumbItem>
            			<BreadcrumbItem active>Book Therapist</BreadcrumbItem>
            		</Breadcrumb>
            		<div className="col-12">
            			<h3>Therapists</h3>
            			<hr />
            		</div>
            	</div>
                <div className="row">
                    {book}
                </div>
                
            </div>
        );
    }  

export default Book;