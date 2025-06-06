# chain_engine.py

def get_next_agent(format, intent):
    """
    Define agent chaining rules here.
    """
    if format == "Email" and intent == "RFQ":
        return "JSONAgent"  # Example: route RFQs to JSONAgent
    if format == "PDF" and intent == "Complaint":
        return "EmailAgent"  # Example: route complaints to email team
    return None
