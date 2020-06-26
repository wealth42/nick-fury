import React from 'react';


//We'll be return loading spinner for loading screen.
export const Loading = () => {
	return(
		<div className="col-12">
            <span className="fa fa-spinner fa-pulse fa-3x fa-fw text-primary"></span>
            <p>Loading . . .</p>
        </div>
	);
};