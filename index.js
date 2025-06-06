const express = require('express');
const app = express();
const langflowRoutes = require('./routes/langflow');

app.use(express.json());
app.use('/api/langflow', langflowRoutes);

const PORT = 3000;
app.listen(PORT, () => console.log(`API server on http://localhost:${PORT}`));
