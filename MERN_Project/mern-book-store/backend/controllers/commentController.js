const Comment = require('../models/Comment');

const addComment = async (req, res) => {
  const { noteId, text } = req.body;
  const comment = await Comment.create({ noteId, userId: req.user._id, text });
  res.status(201).json(comment);
};

const getComments = async (req, res) => {
  const comments = await Comment.find({ noteId: req.params.noteId }).populate('userId', 'name');
  res.json(comments);
};

module.exports = { addComment, getComments };
