const mongoose = require('mongoose');

const sellRequestSchema = new mongoose.Schema({
  userId: { type: mongoose.Schema.Types.ObjectId, ref: 'User' },
  description: String,
  fileUrl: String,
  status: { type: String, default: 'pending' }
});

const SellRequest = mongoose.model('SellRequest', sellRequestSchema);
module.exports = SellRequest;
