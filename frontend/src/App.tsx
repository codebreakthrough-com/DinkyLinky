import { useState } from 'react';
import './App.css'
import { FaRegCopy } from "react-icons/fa";

function App() {

  const baseUrl = "http://localhost:8080/"
  const [url, setUrl] = useState('');
  const [shortUrl, setShortUrl] = useState('');
  const [copied, setCopied] = useState(false);

  const handleCopy = () => {
    
    navigator.clipboard.writeText(shortUrl);
    setCopied(true);
    setTimeout(() => setCopied(false), 1500); // Hide after 1.5 seconds
  };

  const shortenUrl = async (e: React.FormEvent) => {
    e.preventDefault();
    const response = await fetch(baseUrl + "api/urls/", {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ "long_url": url }),
    });
    const data = await response.json();
    setShortUrl(baseUrl + data.short_url);
  }

  return (
    <>
      <h1 id="header">Dinky Linky</h1>
      <form onSubmit={shortenUrl}>
        <input type="url" value={url} onChange={e => setUrl(e.target.value)} placeholder='Enter URL' required/>
        <button type="submit">Shorten</button>
      </form>

      {shortUrl && (
        <div style={{margin: "10px"}}>
          Your short URL is: <a href={shortUrl}>{shortUrl}</a> <FaRegCopy style={{cursor: "pointer", marginLeft: "7px" }} onClick={() => handleCopy()}/> 
          {copied && (
        <span className={copied ? "visible" : "hidden"} style={{ marginLeft: "5px" }}>
          copied!
        </span>
        )}
        </div>
        
      )}
    </>
  )
}

export default App
