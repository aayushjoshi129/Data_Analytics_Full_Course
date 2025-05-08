const express = require('express');
const { createNote, getNotes } = require('../controllers/noteController');
const { protect } = require('../middleware/authMiddleware');
const { addComment, addRating } = require('../controllers/noteController.js');
const router = express.Router();

router.route('/').get(getNotes).post(protect, createNote);
router.post('/comment', protect, addComment);
router.post('/rate', protect, addRating);

module.exports = router;
