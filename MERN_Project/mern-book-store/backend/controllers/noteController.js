const Note = require('../models/Note');
const Comment = require('../models/Comment.js');
const Rating = require('../models/Rating.js');

const createNote = async (req, res) => {
  const note = await Note.create({ ...req.body, uploader: req.user._id });
  res.status(201).json(note);
};

const getNotes = async (req, res) => {
  const notes = await Note.find().populate('uploader', 'name');
  res.json(notes);
};

// Add a Comment
const addComment = async (req, res) => {
  const { noteId, text } = req.body;
  try {
    const newComment = new Comment({
      user: req.user._id,
      note: noteId,
      text,
    });
    await newComment.save();
    res.status(201).json(newComment);
  } catch (error) {
    res.status(400).json({ message: error.message });
  }
};

// Add a Rating
const addRating = async (req, res) => {
  const { noteId, rating } = req.body;
  try {
    const newRating = new Rating({
      user: req.user._id,
      note: noteId,
      rating,
    });
    await newRating.save();
    res.status(201).json(newRating);
  } catch (error) {
    res.status(400).json({ message: error.message });
  }
};

module.exports = { createNote, getNotes, addComment, addRating };
