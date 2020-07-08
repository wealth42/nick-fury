import React, { useState, useEffect } from "react";
import "../styles.css";
import { API } from "../backend";
import  Base  from "./Base";
import { getUsers } from "./helper/coreapicalls";


export default function Home() {
  const [products, setProducts] = useState([]);
  const [error, setError] = useState(false);

 /* const loadAllUsers = () => {
    getUsers().then(data => {
      if (data.error) {
        setError(data.error);
      } else {
        setProducts(data);
      }
    });
  }; 

  useEffect(() => {
    loadAllUsers();
  }, []); */

  return (
    <Base title="Home Page" description="Welcome to Wealth42">
      <h1 className="text-white">All Users</h1>
      <div className="row text-center">
        <div className="row">
              <div className="col-4 mb-4">
                <h1>Here goes the list of users</h1>
              </div>
          )
        </div>
      </div>
    </Base>
  );
}

