import React from "react";
import About from "./About";
import Button from "./Button";

const Navbar = () => {
  return (
    <div className="pagee">
      <div className="headingg">
        <h1 className="headin">Automatic License Plate Recognition</h1>
      </div>
      <About />
      <Button />
    </div>
  );
};

export default Navbar;
