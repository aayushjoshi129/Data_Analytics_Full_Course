const SellRequest = require('../models/SellRequest');

const submitSellRequest = async (req, res) => {
  const { description, fileUrl } = req.body;
  const request = await SellRequest.create({ userId: req.user._id, description, fileUrl });
  res.status(201).json(request);
};

const getSellRequests = async (req, res) => {
  const requests = await SellRequest.find().populate('userId', 'name');
  res.json(requests);
};

module.exports = { submitSellRequest, getSellRequests };
