import React, { useState, useEffect } from 'react';
import './styles.css';

const App = () => {
  const [isRunning, setIsRunning] = useState(false);

  // On start, start the interval check every second to see if the current URL.
  useEffect(() => {
    let interval;
    if (isRunning) {
      interval = setInterval(() => {
        checkCurrentURL();
      }, 1000); // Check every second
    } else {
      clearInterval(interval);
    }
    return () => clearInterval(interval);
  }, [isRunning]);

  // Console log the current state.
  const handleClick = () => {
    setIsRunning(!isRunning);
    if (!isRunning) {
      console.log('Process started!');
    } else {
      console.log('Process stopped!');
    }
  };

  // Checks if current URL matches the github repos url. Then starts the script for chatbot.
  const checkCurrentURL = () => {
    const currentURL = window.location.href;
    const githubPattern = /^https:\/\/github\.com\/[^\/]+\/[^\/]+/;
    if (githubPattern.test(currentURL)) {
      console.log('User is on GitHub Repos:', currentURL);
      // Add your logic here if the URL matches GitHub
    } else {
      console.log('User is not on GitHub Repos.:', currentURL);
    }
  };

  return (
    <div className="container">
      <h1 className="title">Code Reaper LLM</h1>
      <h3>Interpret large codebases and answer questions as a chatbot!</h3>
      <button onClick={handleClick} className="search-button">
        {isRunning ? 'Stop' : 'Start'}
      </button>
      {/*
      {isRunning && (
        <div className="animation">
          // Replace with your actual animation (once created)
        </div>
      */}
    </div>
  );
};

export default App;
