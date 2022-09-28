import './App.css';
import React, { useEffect, useState } from 'react';

function About() {

  const [data, setData] = useState({name: "original"})

  useEffect(() => {
    const fetchData = async () => {
      const result = await fetch("http://backend:8080")
      console.warn("result",result);
      const jsonResult = await result.json()

      setData(jsonResult)
    }

    fetchData()
  }, [])

  console.log("-------------------------------------------------", data)

  return (
    <div className="About">
      <header className="About-header">
        About
      </header>
      <p>
        This is an about of the app. {data.name}
        </p>
    </div>
  );
}

export default About;
