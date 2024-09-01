import React from 'react';
import './styles.css';

const App = () => {
  const handleClick = () => {
    console.log('Button clicked!');
    // Add code to run your script here

  };

  return (
    <div className="container">
      <h1 className="title">Code Reaper LLM</h1>
      <button onClick={handleClick} className="search-button">
        Search Github
      </button>
    </div>
  );
};

export default App;
