const mongoose = require('mongoose');

const ratingSchema = mongoose.Schema(
  {
    user: {
      type: mongoose.Schema.Types.ObjectId,
      required: true,
      ref: 'User',  // Reference to User model
    },
    note: {
      type: mongoose.Schema.Types.ObjectId,
      required: true,
      ref: 'Note',  // Reference to Note model
    },
    rating: {
      type: Number,
      required: true,
      min: 1,
      max: 5,  // Rating between 1 to 5
    },
  },
  {
    timestamps: true,
  }
);

const Rating = mongoose.model('Rating', ratingSchema);
module.exports = Rating;

