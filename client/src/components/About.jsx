import React from "react";
import SES from "./403 Error Forbidden-bro (1).svg";

const About = () => {
  return (
    <div className="container grid-2 aboutt">
      <div>
        <h3 style={{ paddingTop: "30%" }}>
          ALPR for India detects license plates from images of vehicles and
          converts license plate numbers to strings. This can be used by law
          enforcement vehicles to scan, in real time, vehicle insurance expiry,
          pollution check certificate validation, and possible blacklisted
          vehicles on road
        </h3>
      </div>
      <div>
        <img src={SES} alt="SVG here" />
      </div>
    </div>
  );
};

export default About;
