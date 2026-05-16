import { useState } from 'react'
import axios from 'axios'

import './App.css'

function App() {
  const [message, setMessage]=useState("");
  const [response, setResponse]=useState("");

  async function sendMessage(){
    try{
      const res=await axios.post("http://localhost:8000/generate?message="+message);
      setResponse(res.data.response);
    } catch (error) {
      console.error("Error sending message:", error);
    }
  }
  return (
    <div className="App"> 
    <h1>Gemma 4 generate</h1>
    <input type="test" value={message} onChange={(e)=> setMessage(e.target.value)} placeholder="Enter your message"/>
    <button onClick={sendMessage}>Send</button>
    <p>Response: {response}</p>
    </div>
  );

}

export default App

