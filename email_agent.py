from datetime import datetime

class EmailAgent:
    def __init__(self, memory):
        self.memory = memory

    def process(self, email_text, conversation_id):
        print("📨 Email Agent Output:")

        sender = None
        urgency = "Normal"
        intent = "RFQ"  # For simplicity, assume RFQ here; improve as needed.

        for line in email_text.splitlines():
            if line.lower().startswith("from:"):
                sender = line.split(":", 1)[1].strip()
            if "urgent" in line.lower():
                urgency = "High"

        extracted_data = {
            "sender": sender,
            "intent": intent,
            "urgency": urgency,
            "receivedAt": datetime.utcnow().isoformat()
        }

        print(extracted_data)

        self.memory.log(
            source="EmailAgent",
            data_type="Email",
            intent=intent,
            extracted_data=extracted_data,
            conversation_id=conversation_id,
            sender=sender,
            topic=None
        )
