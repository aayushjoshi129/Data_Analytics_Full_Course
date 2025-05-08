// NoteDetail.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const NoteDetail = ({ match }) => {
  const [note, setNote] = useState({});
  const [comments, setComments] = useState([]);
  const [rating, setRating] = useState(0);
  const [commentText, setCommentText] = useState('');

  const noteId = match.params.id;

  useEffect(() => {
    const fetchNote = async () => {
      const { data } = await axios.get(`/api/notes/${noteId}`);
      setNote(data);
    };
    fetchNote();
  }, [noteId]);

  const submitComment = async () => {
    await axios.post('/api/notes/comment', { noteId, text: commentText }, {
      headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },
    });
    setCommentText('');
  };

  const submitRating = async (rate) => {
    await axios.post('/api/notes/rate', { noteId, rating: rate }, {
      headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },
    });
    setRating(rate);
  };

  return (
    <div>
      <h1>{note.title}</h1>
      <div>{note.description}</div>
      {/* Display Comments */}
      <h3>Comments:</h3>
      {comments.map((comment) => (
        <div key={comment._id}>{comment.text}</div>
      ))}
      <textarea value={commentText} onChange={(e) => setCommentText(e.target.value)} />
      <button onClick={submitComment}>Submit Comment</button>
      
      {/* Display Rating */}
      <h3>Rating: {rating}</h3>
      {[1, 2, 3, 4, 5].map((rate) => (
        <button key={rate} onClick={() => submitRating(rate)}>{rate}</button>
      ))}
    </div>
  );
};

export default NoteDetail;
