const express = require('express');
const router = express.Router();

// Get last 50 runs
router.get('/runs', async (req, res) => {
  // TODO: Fetch and return last 50 runs
  res.json([]);
});

// Get run by ID
router.get('/runs/:id', async (req, res) => {
  const runId = req.params.id;
  // TODO: Return full output/logs for runId
  res.json({ id: runId });
});

// Stream logs (SSE)
router.get('/runs/:id/stream', (req, res) => {
  const runId = req.params.id;
  res.setHeader('Content-Type', 'text/event-stream');
  res.setHeader('Cache-Control', 'no-cache');
  res.setHeader('Connection', 'keep-alive');
  // TODO: Stream logs in real-time for runId
  res.write(`data: Stream for run ${runId}\n\n`);
});

// Trigger workflow
router.post('/trigger', async (req, res) => {
  const { workflowId, engine, triggerType, inputPayload } = req.body;
  // TODO: Trigger workflow in LangFlow
  res.json({ success: true });
});

// Public webhook (forward to LangFlow run)
router.post('/hooks/:workflowId', async (req, res) => {
  const { workflowId } = req.params;
  const payload = req.body;
  // TODO: Forward to LangFlow workflow execution
  res.json({ accepted: true, workflowId });
});

module.exports = router;
