import React from 'react';
import { Button } from 'reactstrap';

function Home(props) {
  return (
    <div className="container">
      <Button onClick={() => props.history.push("/clientlogin")}>Client Login</Button>
      <Button onClick={() => props.history.push("/therapistlogin")}>Therapist Login</Button>
    </div>
  );
}

export default Home;
