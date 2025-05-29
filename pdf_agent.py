import re

class PDFAgent:
    def __init__(self, memory):
        self.memory = memory

    def process(self, pdf_text, conversation_id):
        print("📄 PDF Agent extracted text:")
        print(pdf_text)

        invoice_number = self._extract_value(pdf_text, r"Invoice Number:\s*(\d+)")
        date = self._extract_value(pdf_text, r"Date:\s*([0-9\-]+)")
        amount = self._extract_value(pdf_text, r"Amount:\s*(\d+(\.\d+)?)")
        customer = self._extract_value(pdf_text, r"Customer:\s*(.+)")
        description = self._extract_value(pdf_text, r"Description:\s*(.+)")

        result = {
            "invoiceNumber": invoice_number,
            "date": date,
            "amount": float(amount) if amount else None,
            "customer": customer,
            "description": description
        }

        self.memory.log(
            source="PDFAgent",
            data_type="PDF",
            intent="Invoice",
            extracted_data=result,
            conversation_id=conversation_id
        )

    def _extract_value(self, text, pattern):
        match = re.search(pattern, text)
        return match.group(1).strip() if match else None
