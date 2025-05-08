const express = require('express');
const { submitSellRequest, getSellRequests } = require('../controllers/sellRequestController');
const { protect } = require('../middleware/authMiddleware');
const router = express.Router();

router.route('/').post(protect, submitSellRequest).get(protect, getSellRequests);

module.exports = router;
