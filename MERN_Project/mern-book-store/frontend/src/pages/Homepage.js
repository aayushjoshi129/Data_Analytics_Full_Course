import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';

const HomePage = () => {
  const [notes, setNotes] = useState([]);

  // Fetch latest notes from backend
  const fetchNotes = async () => {
    try {
      const res = await axios.get('/api/v1/notes');
      setNotes(res.data.notes.slice(0, 6)); // Show top 6
    } catch (error) {
      console.error('Error fetching notes:', error);
    }
  };

  useEffect(() => {
    fetchNotes();
  }, []);

  return (
    <div className="bg-gray-50 py-12">
      <div className="container mx-auto px-4 sm:px-6 lg:px-8">
        <header className="mb-8 text-center">
          <h1 className="text-4xl font-extrabold text-blue-700 mb-2">Welcome to <span className="text-green-600">e</span>Note<span className="text-purple-600">Share</span></h1>
          <p className="text-lg text-gray-700">
            Discover and share handwritten B.Tech notes, organized by semester.
          </p>
        </header>

        <nav className="flex justify-center space-x-4 mb-8">
          <Link
            to="/login"
            className="inline-block bg-blue-600 hover:bg-blue-700 text-white font-semibold py-3 px-6 rounded-full focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 transition duration-300"
          >
            Login
          </Link>
          <Link
            to="/register"
            className="inline-block bg-green-600 hover:bg-green-700 text-white font-semibold py-3 px-6 rounded-full focus:outline-none focus:ring-2 focus:ring-green-500 focus:ring-offset-2 transition duration-300"
          >
            Register
          </Link>
          <Link
            to="/upload"
            className="inline-block bg-purple-600 hover:bg-purple-700 text-white font-semibold py-3 px-6 rounded-full focus:outline-none focus:ring-2 focus:ring-purple-500 focus:ring-offset-2 transition duration-300"
          >
            Upload Notes
          </Link>
        </nav>

        <section className="mb-8">
          <h2 className="text-3xl font-semibold text-gray-800 mb-4">Latest Notes</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {notes.length > 0 ? (
              notes.map(note => (
                <div key={note._id} className="bg-white rounded-lg shadow-md hover:shadow-lg transition duration-300 overflow-hidden">
                  <div className="p-6">
                    <h3 className="font-bold text-xl text-blue-700 mb-2 truncate">{note.title}</h3>
                    <p className="text-gray-600 text-sm mb-3 line-clamp-2">{note.description}</p>
                    <p className="text-sm text-gray-500 mb-2">Semester: {note.semester}</p>
                    <Link
                      to={`/notes/${note._id}`}
                      className="inline-block bg-blue-500 hover:bg-blue-600 text-white font-semibold py-2 px-4 rounded-full focus:outline-none focus:ring-2 focus:ring-blue-400 focus:ring-offset-2 transition duration-300"
                    >
                      View Note
                    </Link>
                  </div>
                </div>
              ))
            ) : (
              <div className="bg-yellow-100 border-l-4 border-yellow-500 p-4">
                <p className="text-yellow-700">
                  No notes found yet. Be the first to <Link to="/upload" className="font-semibold underline hover:text-yellow-800">upload</Link>!
                </p>
              </div>
            )}
          </div>
        </section>

        <footer className="text-center text-gray-500 mt-8">
          <p>&copy; {new Date().getFullYear()} eNoteShare. All rights reserved.</p>
        </footer>
      </div>
    </div>
  );
};

export default HomePage;