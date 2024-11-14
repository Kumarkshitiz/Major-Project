import React, { useState, useEffect } from "react";
import "./style.css";

function AfterSubmit() {
  const lines = [
    "We are generating your report!",
    "About to generate report!",
    "Report has been generated!",
  ];

  const [currentLine, setCurrentLine] = useState(0);

  useEffect(() => {
    if (currentLine < lines.length - 1) {
      const timer = setTimeout(() => {
        setCurrentLine(currentLine + 1);
      }, 3000); // 3-second delay

      return () => clearTimeout(timer); // Cleanup the timer
    }
  }, [currentLine, lines.length]);

  return (
    <div className="before">
      <div className="after">
        <h1 className="headings">{lines[currentLine]}</h1>
      </div>
    </div>
  );
}

export default AfterSubmit;
