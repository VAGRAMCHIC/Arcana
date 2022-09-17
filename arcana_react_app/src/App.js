import React from "react";

import {
  BrowserRouter as Router,
  Routes,
  Route,
  Link
} from "react-router-dom";

import AuthForm from "./components/auth/AuthForm";
import RegisterForm from "./components/auth/RegisterForm";
import Gallery from "./components/gallery/Gallery";

import './styles/App.css';

function App() {
  return (
    <div className="App bg-black h-full w-full">
      <Router>
        <Routes>
            <Route exact path="/gallery" element={<Gallery/>}/>
            <Route exact path="/login" element={<AuthForm/>}/>
            <Route exact path="/register" element={<RegisterForm/>}/>
          </Routes>
      </Router>
    </div>
  );
}

export default App;
