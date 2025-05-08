const mongoose = require('mongoose');

const noteSchema = new mongoose.Schema({
  title: String,
  description: String,
  subject: String,
  semester: Number,
  branch: String,
  fileUrl: String,
  price: Number,
  uploader: { type: mongoose.Schema.Types.ObjectId, ref: 'User' }
}, { timestamps: true });

const Note = mongoose.model('Note', noteSchema);
module.exports = Note;
