import './App.css';
import React, { useEffect,useState  } from 'react';
import io from 'socket.io-client';

const socket = io("http://localhost:8080");

function MessageLog() {

  return (
    <div className="MessageLog">

    </div>
  );
}

export default About;
