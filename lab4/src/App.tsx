import React from 'react';
import Home from './Home';
import './App.css';

const App: React.FC = () => {
  return (
    <div className="App">
      <h1>Todo List</h1>
      <Home />
    </div>
  );
}

export default App;
