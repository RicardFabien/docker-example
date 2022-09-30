import './App.css';
import React, { useEffect,useState  } from 'react';
import io from 'socket.io-client';

const socket = io("http://localhost:8080");

function About() {

   const [data, setData] = useState([])
   const [username, setUsername] = useState("")
   const [comment, setComment] = useState("")


  useEffect(() => {

    socket.on('connect', () => {
      console.warn("Connected")
    });

    socket.on('message', (message) => {
      setData(d =>[...data, message])
      console.warn("received message", data)
    });

    return () => {
      socket.off('connect');
      socket.off('message');
    };

    
  })

  const sendMessage = () => {
    socket.emit('message', {username, comment});
  }

  return (
    <div className="About">
      <header className="About-header">
        About
      </header>
      
      <p>
        This is an about of the app
        </p>

        {data.map((item, index) => (
         <div key={index}>
          <p>{item.username}: <br/>
          {item.comment}</p>
         </div>
      ))}
      <input
        type="text"
        id="username-input"
        name="text"
        autoComplete="off"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      />
      <br/>
      <textarea
        id="comment-input"
        name="text"
        value={comment}
        onChange={(e) => setComment(e.target.value)}
      />
          <br/>
        <button onClick={ sendMessage }>Send ping</button>
    </div>
  );
}

export default About;
