const User = require('../models/User');
const jwt = require('jsonwebtoken');

const generateToken = id => jwt.sign({ id }, process.env.JWT_SECRET, { expiresIn: '30d' });

const registerUser = async (req, res) => {
  const { name, email, password } = req.body;
  const userExists = await User.findOne({ email });
  if (userExists) return res.status(400).json({ message: 'User exists' });
  console.log("User Exists")
  const user = await User.create({ name, email, password });
  res.status(201).json({ _id: user._id, name: user.name, email: user.email, token: generateToken(user._id) });
  console.log("Registered")

};

const loginUser = async (req, res) => {
  const { email, password } = req.body;
  const user = await User.findOne({ email });
  if (user && await user.matchPassword(password)) {
    console.log("Logged In")
    res.json({ _id: user._id, name: user.name, email: user.email, token: generateToken(user._id) });
  } else {
    console.log("Invalid Credentials")
    res.status(401).json({ message: 'Invalid credentials' });
  }
};

// const getUsers = async (req, res) => {
//   const users = await User.find();
//   if (users.length>0) {
//     res.json(users);
//   } else {
//     res.status(401).json({ message: 'Invalid request' });
//   }
// };

const getUsers = async (req, res) => {
  try {
    // Get all users
    const users = await User.find();
    // const users = await User.find({}, { name: 1, _id: 0 });

    // Check if users exist
    if (users.length > 0) {
      console.log("User Details:")
      res.json(users);  // Respond with all users
    } else {
      console.log("No User Details Found:")
      res.status(404).json({ message: 'No users found' });
    }
  } catch (error) {
    console.log("Server Error:")
    res.status(500).json({ message: 'Server Error' });
  }
};


module.exports = { registerUser, loginUser, getUsers };
