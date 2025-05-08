// server.js
const express = require('express');
const dotenv = require('dotenv');
const cors = require('cors');
const connectDB = require('./config/db');
const userRoutes = require('./routes/userRoutes');
const noteRoutes = require('./routes/noteRoutes');
const commentRoutes = require('./routes/commentRoutes');
const sellRequestRoutes = require('./routes/sellRequestRoutes');

dotenv.config();
const app = express();

connectDB();

// connectDB()
//   .then(() => {
//     console.log('PORT:', process.env.PORT);
//     console.log('MONGO_URI:', process.env.MONGO_URI);
//     console.log('✅ MongoDB Connection Successful'); // First message
//   })

app.use(cors());
app.use(express.json());

app.use('/api/users', userRoutes);
app.use('/api/notes', noteRoutes);
app.use('/api/comments', commentRoutes);
app.use('/api/sell-requests', sellRequestRoutes);

app.get('/', (req, res) => res.send('API Running'));

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
