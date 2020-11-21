import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import Navbar from "./components/Navbar";
import Dragg from "./components/Dragg";
import "./App.css";

const App = () => {
  return (
    <Router>
      <div>
        <Switch>
          <Route exact path="/" component={Navbar}></Route>
          <Route exact path="/main" component={Dragg}></Route>
        </Switch>
      </div>
    </Router>
  );
};

export default App;
