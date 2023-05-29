import React, { useState, useRef, useEffect } from "react";
import Modal from "react-modal";
import { FaTimes } from "react-icons/fa";
import "./Droid.css";
import droidIcon from "../../assets/droidIcon.png";

Modal.setAppElement("#root");

const Droid = () => {
  const [isChatOpen, setIsChatOpen] = useState(false);
  const [message, setMessage] = useState("");
  const [chatHistory, setChatHistory] = useState([]);
  const [isDefaultMessageSent, setIsDefaultMessageSent] = useState(false);
  const chatContainerRef = useRef(null);

  const openChat = () => {
    setIsChatOpen(true);
    if (!isDefaultMessageSent) {
      sendDefaultMessage();
      setIsDefaultMessageSent(true);
    }
  };

  const closeChat = () => {
    setIsChatOpen(false);
  };

  const sendMessage = (msg, sender) => {
    const newMessage = {
      text: msg,
      sender: sender,
    };

    setChatHistory((prevChatHistory) => [...prevChatHistory, newMessage]);
  };

  const sendDefaultMessage = () => {
    sendMessage("Olá! Como posso ajudar?", "bot");
  };

  const handleInputChange = (e) => {
    setMessage(e.target.value);
  };

  const handleInputKeyPress = (e) => {
    if (e.key === "Enter" && message.trim() !== "") {
      e.preventDefault();
      sendMessage(message, "user");
      setMessage("");
    }
  };

  const handleSend = () => {
    if (message.trim() !== "") {
      sendMessage(message, "user");
      setMessage("");
    }
  };

  useEffect(() => {
    if (chatContainerRef.current) {
      chatContainerRef.current.scrollTop =
        chatContainerRef.current.scrollHeight;
    }
  }, [chatHistory]);

  useEffect(() => {
    if (isChatOpen && chatContainerRef.current) {
      chatContainerRef.current.scrollTop =
        chatContainerRef.current.scrollHeight;
    }
  }, [isChatOpen]);

  const ChatHeader = ({ onClose }) => (
    <div className="chat-header">
      <img src={droidIcon} alt="Chat Icon" className="header-icon" />
      <button className="close-button" onClick={onClose}>
        <FaTimes />
      </button>
    </div>
  );

  const ChatMessage = ({ chat }) => (
    <div className={`message ${chat.sender}`}>
      {chat.sender === "bot" && (
        <img src={droidIcon} alt="Bot Icon" className="message-icon" />
      )}
      {chat.text}
    </div>
  );

  const ChatInput = ({ message, onInputChange, onInputKeyPress, onSend }) => (
    <div className="chat-input">
      <input
        type="text"
        value={message}
        onChange={onInputChange}
        onKeyPress={onInputKeyPress}
        placeholder="Digite uma mensagem"
      />
      <button onClick={onSend}>Enviar</button>
    </div>
  );

  const chatContainerClass =
    chatHistory.length > 10 ? "chat-messages chat-scrollable" : "chat-messages";

  return (
    <>
      <Modal
        isOpen={isChatOpen}
        onRequestClose={closeChat}
        className="chat-modal"
        overlayClassName="chat-overlay"
      >
        <div className="chat-container">
          <ChatHeader onClose={closeChat} />
          <div className={chatContainerClass} ref={chatContainerRef}>
            {chatHistory.slice(-10).map((chat, index) => (
              <ChatMessage key={index} chat={chat} />
            ))}
          </div>
          <ChatInput
            message={message}
            onInputChange={handleInputChange}
            onInputKeyPress={handleInputKeyPress}
            onSend={handleSend}
          />
        </div>
      </Modal>
      <div className="chat-icon" onClick={openChat}>
        <img src={droidIcon} alt="Chat Icon" />
      </div>
    </>
  );
};

export default Droid;
