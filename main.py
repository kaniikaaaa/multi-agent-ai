from memory_module import SQLiteMemory
from agents.classifier_agent import ClassifierAgent
from agents.json_agent import JSONAgent
from agents.email_agent import EmailAgent
from agents.pdf_agent import PDFAgent
from memory.sqlite_memory import SQLiteMemory


def main():
    # Initialize shared memory
    memory = SQLiteMemory("memory.db")

    # Initialize agents with shared memory
    json_agent = JSONAgent(memory)
    email_agent = EmailAgent(memory)
    pdf_agent = PDFAgent(memory)
    classifier = ClassifierAgent(memory, json_agent, email_agent, pdf_agent)

    # Sample inputs
    sample_json = {
        "invoiceId": "12345",
        "intent": "Invoice",
        "sender": "accounts@example.com",
        "topic": "May Invoice"
    }

    sample_email = """From: buyer@example.com
Subject: Urgent RFQ for office chairs

Please send us a quote for 20 office chairs ASAP."""

    sample_pdf_text = """Invoice Number: 12345
Date: 2025-05-10
Amount: 1000
Customer: ABC Pvt Ltd
Description: Purchase of office chairs"""

    print("🧪 Testing JSON Input...")
    classifier.classify(sample_json)

    print("\n🧪 Testing Email Input...")
    classifier.classify(sample_email)

    print("\n🧪 Testing PDF Input...")
    classifier.classify(sample_pdf_text)

    # 🔍 Fetch and display logs from the last conversation
    print("\n🔍 Fetching logs for the last conversation...\n")

    # Get the latest conversation ID from logs
    last_convo_row = memory.conn.execute(
        "SELECT conversation_id FROM logs WHERE conversation_id IS NOT NULL ORDER BY timestamp DESC LIMIT 1"
    ).fetchone()

    if last_convo_row:
        conversation_id = last_convo_row[0]
        logs = memory.fetch_logs_by_conversation(conversation_id)
        for log in logs:
            print(f"[{log['timestamp']}] {log['source']} → {log['intent']}")
            print(f"   Extracted: {log['extracted_data']}\n")
    else:
        print("No conversation logs found.")

if __name__ == "__main__":
    main()
