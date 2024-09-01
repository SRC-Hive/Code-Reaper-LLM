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
      <h3>Interpret large codebases and answers questions as a chatbot!</h3>
      <button onClick={handleClick} className="search-button">
        Search Github
      </button>
    </div>
  );
};

export default App;
