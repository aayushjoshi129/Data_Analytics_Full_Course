const express = require('express');
const { addComment, getComments } = require('../controllers/commentController');
const { protect } = require('../middleware/authMiddleware');
const router = express.Router();

router.route('/:noteId').get(getComments);
router.route('/').post(protect, addComment);

module.exports = router;
