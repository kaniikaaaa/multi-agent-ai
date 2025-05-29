# Multi-Agent AI System

## Overview
This project implements a multi-agent AI system capable of processing input in **PDF**, **JSON**, or **Email (text)** formats. It classifies the format and intent, then routes the input to specialized agents for processing. Shared context is maintained using an SQLite database for traceability and chaining.

## Features
- **Classifier Agent:** Detects input format (PDF, JSON, Email) and intent (Invoice, RFQ, etc.).
- **JSON Agent:** Parses and validates JSON invoice data.
- **Email Agent:** Extracts sender, intent, and urgency from email text.
- **PDF Agent:** Extracts invoice details using regex from PDF text content.
- **Shared Memory:** Uses SQLite to store logs and context across agents.
- **Query Support:** Fetch and trace conversation logs from memory.

## Getting Started

### Prerequisites
- Python 3.7+
- `sqlite3` (comes standard with Python)

