import React from 'react';
import './styles.css';

const App = () => {
  const handleClick = () => {
    console.log('Button clicked!');
    // Add code to run your script here
  };

  return (
    <div>
      <h1>Code Reaper LLM</h1>
      <button onClick={handleClick}>Search Github</button>
    </div>
  );
};

export default App;
