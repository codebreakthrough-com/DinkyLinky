import { useState } from 'react';
import './App.css'

function App() {

  const baseUrl = "http://localhost:8080/api/"
  const [url, setUrl] = useState('');
  const [shortUrl, setShortUrl] = useState('');

  const shortenUrl = async (e: React.FormEvent) => {
    e.preventDefault();
    const response = await fetch(baseUrl + "urls/", {
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
      <h1>Dinky Linky</h1>
      <form onSubmit={shortenUrl}>
        <input type="url" value={url} onChange={e => setUrl(e.target.value)} placeholder='Enter URL' required/>
        <button type="submit">Shorten</button>
      </form>

      {shortUrl && (
        <p className="mt-4">
          Your short URL is: <a href={shortUrl}>{shortUrl}</a>
        </p>
      )}
    </>
  )
}

export default App
