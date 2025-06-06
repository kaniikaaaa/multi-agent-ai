const express = require('express');
const app = express();
const port = process.env.PORT || 3000;

app.use(express.json());

// Import langflow routes
const langflowRoutes = require('./routes/langflow');
app.use('/api/langflow', langflowRoutes);

app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
