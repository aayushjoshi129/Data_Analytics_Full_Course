import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';

const ViewNote = () => {
  const { id } = useParams();
  const [note, setNote] = useState(null);

  useEffect(() => {
    const fetchNote = async () => {
      const { data } = await axios.get('/api/notes');
      const found = data.find(n => n._id === id);
      setNote(found);
    };
    fetchNote();
  }, [id]);

  if (!note) return <div>Loading...</div>;

  return (
    <div className='p-4 max-w-2xl mx-auto'>
      <h1 className='text-2xl font-bold'>{note.title}</h1>
      <p>{note.description}</p>
      <p className='text-sm'>Subject: {note.subject}, Semester: {note.semester}</p>
      <a href={note.fileUrl} target='_blank' rel='noreferrer' className='text-blue-500 underline mt-2 block'>View File</a>
      <p className='mt-2'>Price: ₹{note.price}</p>
    </div>
  );
};
export default ViewNote;