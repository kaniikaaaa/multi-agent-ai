import uuid

class ClassifierAgent:
    def __init__(self, memory, json_agent, email_agent, pdf_agent):
        self.memory = memory
        self.json_agent = json_agent
        self.email_agent = email_agent
        self.pdf_agent = pdf_agent

    def classify(self, raw_input):
        format = None
        intent = None
        sender = None
        topic = None

        # Detect input type
        if isinstance(raw_input, dict):  # JSON input
            format = "JSON"
            intent = raw_input.get('intent', 'Unknown')
            sender = raw_input.get('sender')
            topic = raw_input.get('topic')
        elif isinstance(raw_input, str):
            if raw_input.strip().startswith("Invoice Number"):
                format = "PDF"
                intent = "Invoice"
            elif "From:" in raw_input and "Subject:" in raw_input:
                format = "Email"
                intent = "RFQ"
                sender = self._extract_sender_from_email(raw_input)
                topic = self._extract_subject_from_email(raw_input)
            else:
                format = "Unknown"
                intent = "Unknown"
        else:
            format = "Unknown"
            intent = "Unknown"

        # Generate a conversation ID
        conversation_id = str(uuid.uuid4())

        # Log the classification event
        self.memory.log(
            source="ClassifierAgent",
            data_type=format,
            intent=intent,
            extracted_data=None,
            sender=sender,
            topic=topic,
            conversation_id=conversation_id
        )

        # Route to appropriate agent
        if format == "JSON":
            self.json_agent.process(raw_input, conversation_id)
        elif format == "Email":
            self.email_agent.process(raw_input, conversation_id)
        elif format == "PDF":
            self.pdf_agent.process(raw_input, conversation_id)
        else:
            print("Unknown format, cannot route")

    def _extract_sender_from_email(self, email_text):
        for line in email_text.splitlines():
            if line.lower().startswith("from:"):
                return line.split(":", 1)[1].strip()
        return None

    def _extract_subject_from_email(self, email_text):
        for line in email_text.splitlines():
            if line.lower().startswith("subject:"):
                return line.split(":", 1)[1].strip()
        return None
