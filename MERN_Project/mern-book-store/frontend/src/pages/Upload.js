import React, { useState } from 'react';
import axios from 'axios';
import { useSelector } from 'react-redux';

const Upload = () => {
  const [noteData, setNoteData] = useState({ title: '', description: '', subject: '', semester: '', branch: '', fileUrl: '', price: 0 });
  const token = useSelector(state => state.auth.token);

  const handleSubmit = async (e) => {
    e.preventDefault();
    await axios.post('/api/notes', noteData, { headers: { Authorization: `Bearer ${token}` } });
    alert('Note uploaded');
  };

  return (
    <form onSubmit={handleSubmit} className='p-4 max-w-xl mx-auto'>
      <h2 className='text-xl font-bold mb-4'>Upload Note</h2>
      {Object.keys(noteData).map(key => (
        key !== 'fileUrl' && (
          <input
            key={key}
            className='input mt-2'
            placeholder={key.charAt(0).toUpperCase() + key.slice(1)}
            value={noteData[key]}
            onChange={(e) => setNoteData({ ...noteData, [key]: e.target.value })}
          />
        )
      ))}
      <input type='text' placeholder='File URL' className='input mt-2' value={noteData.fileUrl} onChange={(e) => setNoteData({ ...noteData, fileUrl: e.target.value })} required />
      <button type='submit' className='btn mt-4'>Upload</button>
    </form>
  );
};
export default Upload;