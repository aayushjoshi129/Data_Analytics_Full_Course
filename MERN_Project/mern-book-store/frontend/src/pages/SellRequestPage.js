import React, { useState } from 'react';
import axios from 'axios';

const SellRequestPage = () => {
  const [noteId, setNoteId] = useState('');
  
  const submitRequest = async () => {
    await axios.post('/api/sellrequests', { noteId }, {
      headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },
    });
  };

  return (
    <div>
      <h3>Submit Sell Request</h3>
      <input
        type="text"
        placeholder="Note ID"
        value={noteId}
        onChange={(e) => setNoteId(e.target.value)}
      />
      <button onClick={submitRequest}>Submit Request</button>
    </div>
  );
};

export default SellRequestPage;
