import React, { useState, useRef, useEffect } from "react";
import Modal from "react-modal";
import { FaTimes } from "react-icons/fa";
import "./Droid.css";
import droidIcon from "../../assets/droidIcon.png";
import axios from "axios";
import clearIMG from "../../assets/clear.png";

Modal.setAppElement("#root");

const Droid = () => {
  const [isChatOpen, setIsChatOpen] = useState(false);
  const [chatHistory, setChatHistory] = useState([]);
  const [lastUserMessage, setLastUserMessage] = useState("");
  const chatContainerRef = useRef(null);
  const [selectedOption, setSelectedOption] = useState("");

  const openChat = () => {
    setIsChatOpen(true);
  };

  const closeChat = () => {
    setChatHistory([]);
    setSelectedOption("");
    setIsChatOpen(false);
  };


  const clearChatHistory = () => {
    setChatHistory([]);
    sendInitialMessage();
  };

  const sendInitialMessage = () => {
    axios
      .get("http://127.0.0.1:5000/introducao")
      .then((response) => {
        const { mensagem } = response.data;
        sendMessage(mensagem, "bot");
        scrollToBottom();
      })
      .catch((error) => {
        console.error(error);
        sendMessage(
          "Ocorreu um erro ao carregar as opções. Por favor, tente novamente.",
          "bot"
        );
        scrollToBottom();
      });
  };

  const sendMessage = (msg, sender) => {
    setChatHistory((prevChatHistory) => [
      ...prevChatHistory,
      { text: msg, sender: sender },
    ]);

    if (sender === "user" && (msg === "1" || msg === "2" || msg === "3")) {
      handleChoice(msg);
      return;
    }

    if (sender === "user" && selectedOption === "1") {
      fetch("http://127.0.0.1:5000/duvida", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ question: msg }),
      })
        .then((response) => response.json())
        .then((data) => {
          const botMessage = {
            text: data.response,
            sender: "bot",
          };
          setChatHistory((prevChatHistory) => [...prevChatHistory, botMessage]);
          scrollToBottom();
        })
        .catch((error) => {
          const errorMessage = {
            text: "Ocorreu um erro ao processar sua mensagem. Por favor, tente novamente.",
            sender: "bot",
          };
          setChatHistory((prevChatHistory) => [
            ...prevChatHistory,
            errorMessage,
          ]);
          console.error(error);
          scrollToBottom();
        });
    }
  };
  
  function handleChoice(choice) {
    fetch(`http://127.0.0.1:5000/escolha?valor=${choice}`)
      .then((response) => response.json())
      .then((data) => {
        const mensagem = data.mensagem;
        sendMessage(mensagem, "bot");
        scrollToBottom();

        if (choice === "1") {
          setSelectedOption("1");
        }else if (choice === "2") {
        prospectos(); 
      }
      })
      .catch((error) => {
        console.error(error);
        sendMessage(
          "Ocorreu um erro ao processar sua escolha. Por favor, tente novamente.",
          "bot"
        );
        scrollToBottom();
      });
  }
  
  const prospectos = () => {
    fetch("http://127.0.0.1:5000/prospectos")
      .then((response) => {
        if (!response.ok) {
          throw new Error("Erro ao carregar a lista de prospectos");
        }
        return response.json();
      })
      .then((data) => {
        const { prospectos } = data;
        const prospectosMessage = prospectos.join("\n");
        sendMessage(`Lista de Prospectos:\n${prospectosMessage}`, "bot");
        scrollToBottom();
      })
      .catch((error) => {
        console.error(error);
        sendMessage(
          "Ocorreu um erro ao carregar a lista de prospectos. Por favor, tente novamente.",
          "bot"
        );
        scrollToBottom();
      });
  };
  const Sumarizar = () => {
    const id = idRef.current.value;
    fetch(`/sumarizar?id=${id}`)
      .then((response) => {
        if (!response.ok) {
          throw new Error(`Erro na solicitação: ${response.status}`);
        }
        return response.json();
      })
      .then((data) => {
        setResultado(data);
        setError(null);
      })
      .catch((error) => {
        setError(error.message);
        setResultado(null);
      });
  }
  
  const scrollToBottom = () => {
    if (chatContainerRef.current) {
      chatContainerRef.current.scrollTop = chatContainerRef.current.scrollHeight;
    }
  };

  useEffect(() => {
    if (isChatOpen) {
      sendInitialMessage();
    }
  }, [isChatOpen]);

  useEffect(() => {
    scrollToBottom();
  }, [chatHistory]);

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
      <div
        dangerouslySetInnerHTML={{ __html: chat.text.replace(/\n/g, "<br>") }}
      />
    </div>
  );

  const ChatInput = ({ onSendMessage }) => {
    const [message, setMessage] = useState("");

    const handleInputChange = (e) => {
      setMessage(e.target.value);
    };

    const handleInputKeyPress = (e) => {
      if (e.key === "Enter" && message.trim() !== "") {
        e.preventDefault();
        onSendMessage(message, "user");
        setMessage("");
      }
    };

    const handleSend = () => {
      if (message.trim() !== "") {
        onSendMessage(message, "user");
        setMessage("");
      }
    };

    return (
      <div className="chat-input">
        <input
          type="text"
          value={message}
          onChange={handleInputChange}
          onKeyPress={handleInputKeyPress}
          placeholder="Digite uma mensagem"
        />
        <button onClick={handleSend}>Enviar</button>
      </div>
    );
  };

  return (
    <div>
      <div className="chat-icon" onClick={openChat}>
        <img src={droidIcon} alt="Chat Icon" />
      </div>
      <Modal
        isOpen={isChatOpen}
        onRequestClose={closeChat}
        className="chat-modal"
        overlayClassName="chat-overlay"
      >
        <ChatHeader onClose={closeChat} />
        <div className="chat-container" ref={chatContainerRef}>
          <div className="chat-messages">
            <div className="chat-scrollable">
              {chatHistory.map((chat, index) => (
                <ChatMessage key={index} chat={chat} />
              ))}
            </div>
          </div>
          <ChatInput onSendMessage={sendMessage} />
          <button className="button-container" onClick={clearChatHistory}>
        <img className="clear-icon" src={clearIMG}/>
        </button>
        </div>
      </Modal>
    </div>
  );
};

export default Droid;
