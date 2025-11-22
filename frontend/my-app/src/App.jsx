import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import Navbar from "./components/Navbar";
import Home from "./pages/Home";
import Dashboard from "./pages/Dashboard";
import Predict from "./pages/Predict";
import About from "./pages/About";
import Feedback from "./pages/Feedback";

const App = () => (
  <BrowserRouter>
    <Navbar />
    <Routes>
      <Route path="/" element={<Navigate to="/home" replace />} />
      <Route path="/home" element={<Home />} />
      <Route path="/dashboard" element={<Dashboard />} />
      <Route path="/predict" element={<Predict />} />
      <Route path="/about" element={<About />} />
      <Route path="/feedback" element={<Feedback />} />
    </Routes>
  </BrowserRouter>
);

export default App;
