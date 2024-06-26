import './App.css';
import Home  from './components/pages/Home';
import Login from './components/pages/Login';
import LoginFailed from './components/pages/LoginFailed';
import Register from './components/pages/Register';
import NotFound from './components/pages/NotFound';
import { Routes, Route } from 'react-router-dom';

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/loginfailed" element={<LoginFailed />} />
        <Route path="/register" element={<Register />} />
        <Route path="/notfound" element={<NotFound />} />
      </Routes>
    </div>
  );
}

export default App;
