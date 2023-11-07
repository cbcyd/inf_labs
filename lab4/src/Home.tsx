// Importing necessary modules
import React, { useState, useEffect } from 'react';
import styled from 'styled-components';

// Styled components for the dark glassmorphism effect
const DarkGlassmorphism = styled.div`
  background: rgba(0, 0, 0, 0.25);
  box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
  backdrop-filter: blur(4px);
  -webkit-backdrop-filter: blur(4px);
  border-radius: 10px;
  border: 1px solid rgba(255, 255, 255, 0.18);
  padding: 20px;
  color: #fff;
  width: 50%;
  margin: 0 auto;
  overflow: auto;
`;

const Input = styled.input`
`;

const Button = styled.button`
`;

// Interface for the Todo object
interface Todo {
  id: number;
  name: string;
  completed: boolean;
}

// Functional component for the Home page
const Home: React.FC = () => {
  // State for the todos, new todo, filter, and sort
  const [todos, setTodos] = useState<Todo[]>([]);
  const [newTodo, setNewTodo] = useState<string>('');
  const [filter, setFilter] = useState<string>('all');
  const [sort, setSort] = useState<string>('none');

  // Effect to load todos from local storage on component mount
  useEffect(() => {
    const storedTodos = localStorage.getItem('todos');
    if (storedTodos) {
      setTodos(JSON.parse(storedTodos));
    }
  }, []);

  // Effect to save todos to local storage whenever they change
  useEffect(() => {
    localStorage.setItem('todos', JSON.stringify(todos));
  }, [todos]);

  // Function to handle adding a new todo
  const handleAddTodo = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    if (newTodo) {
      setTodos([...todos, { id: Date.now(), name: newTodo, completed: false }]);
      setNewTodo('');
    }
  };

  // Function to handle removing a todo
  const handleRemoveTodo = (id: number) => {
    setTodos(todos.filter(todo => todo.id !== id));
  };

  // Function to handle toggling the completion status of a todo
  const handleToggleTodo = (id: number) => {
    setTodos(
      todos.map(todo =>
        todo.id === id ? { ...todo, completed: !todo.completed } : todo
      )
    );
  };

  // Function to handle changing the filter
  const handleFilterChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    setFilter(e.target.value);
  };

  // Function to handle changing the sort order
  const handleSortChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    setSort(e.target.value);
    if (e.target.value === 'time') {
      setTodos(todos.sort((a, b) => a.id - b.id));
    } else if (e.target.value === 'none') {
      setTodos(todos);
    }
  };

  // Function to handle exporting todos
  const handleExport = () => {
    const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(todos));
    const downloadAnchorNode = document.createElement('a');
    downloadAnchorNode.setAttribute("href", dataStr);
    downloadAnchorNode.setAttribute("download", "todos.json");
    document.body.appendChild(downloadAnchorNode);
    downloadAnchorNode.click();
    downloadAnchorNode.remove();
  };

  // Function to handle importing todos
  const handleImport = (e: React.ChangeEvent<HTMLInputElement>) => {
    const reader = new FileReader();
    reader.onload = (e) => {
      if (e.target?.result) {
        setTodos(JSON.parse(e.target.result as string));
      }
    };
    if (e.target.files) {
      reader.readAsText(e.target.files[0]);
    }
  };

  // Filtered and sorted todos
  const filteredTodos = todos.filter(todo => {
    if (filter === 'all') return true;
    if (filter === 'completed' && todo.completed) return true;
    if (filter === 'active' && !todo.completed) return true;
    return false;
  });

  const sortedTodos = filteredTodos.sort((a, b) => {
    if (sort === 'name') {
      return a.name.localeCompare(b.name);
    }
    return 0;
  });

  // Render method
  return (
    <DarkGlassmorphism>
      <div>
        <form onSubmit={handleAddTodo}>
          <Input
            type="text"
            value={newTodo}
            onChange={e => setNewTodo(e.target.value)}
            placeholder="Todo to add"
          />
          <Button type="submit">Add</Button>
        </form>
        <select onChange={handleFilterChange}>
          <option value="all">All</option>
          <option value="completed">Completed</option>
          <option value="active">Active</option>
        </select>
        <select onChange={handleSortChange}>
          <option value="time">Time</option>
          <option value="name">Name</option>
        </select>
        <ul>
          {sortedTodos.map(todo => (
            <li key={todo.id}>
              <input
                type="checkbox"
                checked={todo.completed}
                onChange={() => handleToggleTodo(todo.id)}
              />
              {todo.name}
              <Button onClick={() => handleRemoveTodo(todo.id)}>X</Button>
            </li>
          ))}
        </ul>
        <Button onClick={handleExport}>Export</Button>
        <label htmlFor="file-upload">
          Import
        </label>
        <input id="file-upload" type="file" onChange={handleImport} style={{display: "none"}}/>
      </div>
    </DarkGlassmorphism>
  );
};

// Exporting the Home component
export default Home;