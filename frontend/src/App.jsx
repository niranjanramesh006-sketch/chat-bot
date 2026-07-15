import { useState } from "react";
import axios from "axios";

function App() {
  const [message, setMessage] = useState("");
  const [reply, setReply] = useState("");

  const sendMessage = async () => {
  try {
    const response = await fetch("https://unseemly-tackiness-spearfish.ngrok-free.dev/chat", {
      method: "POST",   
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        message: message,
      }),
    });

    const data = await response.json();
    setReply(data.reply);
  } catch (err) {
    console.error(err);
    setReply("❌ Failed to connect to Chota AI");
  }
};

  return (
    <div
      style={{
        background: "#121212",
        color: "white",
        height: "100vh",
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <h1>🤖 Chota AI</h1>

      <input
        type="text"
        placeholder="Ask me anything..."
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        style={{
          width: "350px",
          padding: "12px",
          borderRadius: "8px",
        }}
      />

      <button
        onClick={sendMessage}
        style={{
          marginTop: "20px",
          padding: "10px 20px",
        }}
      >
        Send
      </button>

      <h2 style={{ marginTop: "40px" }}>AI Reply</h2>

      <p>{reply}</p>
    </div>
  );
}
 
export default App;  