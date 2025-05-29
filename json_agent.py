import json

class JSONAgent:
    def __init__(self, memory):
        self.memory = memory

    def process(self, json_data, conversation_id):
        print("🧾 JSON Agent Output:")
        if isinstance(json_data, str):
            json_data = json.loads(json_data)

        invoice_id = json_data.get("invoiceId")
        total_amount = json_data.get("totalAmount")
        invoice_date = json_data.get("invoiceDate")
        missing_fields = []

        if not total_amount:
            missing_fields.append("totalAmount")
        if not invoice_date:
            missing_fields.append("invoiceDate")

        result = {
            "invoiceId": invoice_id,
            "totalAmount": total_amount,
            "invoiceDate": invoice_date,
            "missingFields": missing_fields or None
        }

        print(result)

        self.memory.log(
            source="JSONAgent",
            data_type="JSON",
            intent=json_data.get("intent", "Unknown"),
            extracted_data=result,
            conversation_id=conversation_id
        )
