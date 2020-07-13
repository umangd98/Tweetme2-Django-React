import React from 'react';
import logo from './logo.svg';
import './App.css';
import { TweetsComponents } from '../src/tweets/index';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <TweetsComponents />
      </header>
    </div>
  );
}

export default App;
