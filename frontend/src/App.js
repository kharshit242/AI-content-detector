import React, { useState } from "react";
import axios from "axios";

function App() {
  const [text, setText] = useState("");
  const [result, setResult] = useState("");

  const checkText = async () => {
    try {
      const response = await axios.post(`${process.env.REACT_APP_BACKEND_URL}/check`, { text });
      setResult(response.data.result);
    } catch (error) {
      console.error("Error checking text:", error);
      setResult("Error processing request.");
    }
  };

  return (
    <div style={{ textAlign: "center", padding: "20px" }}>
      <h1>AI Text Detector</h1>
      <textarea
        rows="5"
        cols="50"
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Enter text here..."
      />
      <br />
      <button onClick={checkText}>Check</button>
      <h2>Result: {result}</h2>
    </div>
  );
}

export default App;
