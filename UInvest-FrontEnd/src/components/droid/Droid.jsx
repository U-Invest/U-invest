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
  const idRef = useRef();
  const [context, setContext] = useState(null);

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

    if (sender === "user") {
      if (context === "choose_prospect" && /^[0-9]+$/.test(msg)) {
        fetchProspectDetail(msg);
        setContext(null);
        return;
      } else if (msg === "1" || msg === "2" || msg === "3") {
        handleChoice(msg);
        return;
      }
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
    if (choice === "3") {
      axios.get('http://127.0.0.1:5000/pagina')
        .then(response => {
          const message = response.data.message;
          sendMessage(message, "bot");
          scrollToBottom();
        })
        .catch(error => {
          console.error(error);
          sendMessage(
            "Ocorreu um erro ao tentar abrir o site. Por favor, tente novamente.",
            "bot"
          );
          scrollToBottom();
        });
    } else {
      fetch(`http://127.0.0.1:5000/escolha?valor=${choice}`)
        .then((response) => response.json())
        .then((data) => {
          const mensagem = data.mensagem;
          sendMessage(mensagem, "bot");
          scrollToBottom();

          if (choice === "1") {
            setSelectedOption("1");
          } else if (choice === "2") {
            prospectos();
            setContext("choose_prospect");
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
  
  const scrollToBottom = () => {
    if (chatScrollableRef.current) {
        chatScrollableRef.current.scrollTop = chatScrollableRef.current.scrollHeight;
    }
};

const fetchProspectDetail = (id) => {
  fetch(`http://127.0.0.1:5000/sumarizar?id=${id}`)
    .then((response) => response.json())
    .then((data) => {
      sendMessage(`Detalhes do Prospecto ${id}:\n${JSON.stringify(data)}`, "bot");
      scrollToBottom();
    })
    .catch((error) => {
      console.error(error);
      sendMessage(
        "Ocorreu um erro ao buscar os detalhes do prospecto. Por favor, tente novamente.",
        "bot"
      );
      scrollToBottom();
    });
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

  const chatScrollableRef = useRef(null);

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
          <div className="chat-scrollable" ref={chatScrollableRef}>
              {chatHistory.map((chat, index) => (
                <ChatMessage key={index} chat={chat} />
              ))}
            </div>
          </div>
          <ChatInput onSendMessage={sendMessage} />
          <button className="button-container" onClick={clearChatHistory}>
{/*         <img className="clear-icon" src={clearIMG}/> */}
        </button>
        </div>
      </Modal>
    </div>
  );
};

export default Droid;
