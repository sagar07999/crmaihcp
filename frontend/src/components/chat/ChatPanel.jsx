import { useState } from "react";
import API from "../../services/api";

function ChatPanel() {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState([]);

  const handleSend = async () => {
    if (!input.trim()) return;

    // Add user message
    setMessages((prev) => [
      ...prev,
      { role: "user", text: input },
    ]);

    try {
      const res = await API.post("/chat/", {
        input: input,
      });
      window.dispatchEvent(new Event("refreshInteractions"));
      const data = res.data;

setMessages((prev) => [
  ...prev,
  {
    role: "assistant",
    text: data.message,
  },
]);

      setInput("");

    } catch (err) {
      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          text: "Error contacting AI",
        },
      ]);
    }
  };

  return (
    <div className="card shadow-sm h-100">

      <div className="card-header bg-primary text-white">
        🤖 AI Assistant
      </div>

      <div
        className="card-body"
        style={{
          height: "500px",
          overflowY: "auto",
        }}
      >
        {messages.map((msg, index) => (
          <div
            key={index}
            className={
              msg.role === "user"
                ? "text-end mb-3"
                : "text-start mb-3"
            }
          >
            <div
              className={
                msg.role === "user"
                  ? "alert alert-primary"
                  : "alert alert-success"
              }
            >
              <pre
                style={{
                  whiteSpace: "pre-wrap",
                  margin: 0,
                }}
              >
                {msg.text}
              </pre>
            </div>
          </div>
        ))}
      </div>

      <div className="card-footer">

        <textarea
          rows="3"
          className="form-control"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Describe your interaction..."
        />

        <button
          className="btn btn-success w-100 mt-3"
          onClick={handleSend}
        >
          AI Log Interaction
        </button>

      </div>
    </div>
  );
}

export default ChatPanel;