import React from "react";
import { Routes, Route } from "react-router-dom";
import Header from "./Layout/Header";
import Main from "./pages/Main";
import SignUp from "./pages/SignUp";
import Login from "./pages/Login";
import "./App.css";

const App = () => {
  return (
    <React.Fragment>
      <Header />
      <Routes>
        <Route path="/" element={<Main />} />
        <Route path="/register" element={<SignUp />} />
        <Route path="/login" element={<Login />} />
      </Routes>
    </React.Fragment>
  );
};
export default App;
