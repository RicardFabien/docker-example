import './App.css';
import React, { useEffect } from 'react';
import io from 'socket.io-client';

const socket = io("http://localhost:8080");

function About() {

  // const [data, setData] = useState({name: "original"})

  useEffect(() => {

    socket.on('connect', () => {
      console.warn("Connected")
    });

    socket.on('message', (message) => {
      console.warn("received message", message)
    });

    return () => {
      socket.off('connect');
      socket.off('message');
    };

    
  }, [])

  const sendMessage = () => {
    socket.emit('message', "This is a message");
  }

  return (
    <div className="About">
      <header className="About-header">
        About
      </header>
      <p>
        This is an about of the app.z {/*data.name*/}
        </p>
        <button onClick={ sendMessage }>Send ping</button>
    </div>
  );
}

export default About;
