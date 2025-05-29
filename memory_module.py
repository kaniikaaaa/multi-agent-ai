import sqlite3
from datetime import datetime
import uuid

class SQLiteMemory:
    def __init__(self, db_path="memory.db"):
        self.conn = sqlite3.connect(db_path)
        self._create_table()

    def _create_table(self):
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS logs (
                id TEXT PRIMARY KEY,
                timestamp TEXT,
                source TEXT,
                data_type TEXT,
                intent TEXT,
                extracted_data TEXT,
                conversation_id TEXT,
                sender TEXT,
                topic TEXT
            )
        ''')
        self.conn.commit()

    def log(self, source, data_type, intent, extracted_data, conversation_id=None, sender=None, topic=None):
        entry_id = str(uuid.uuid4())
        timestamp = datetime.utcnow().isoformat()
        self.conn.execute('''
            INSERT INTO logs (id, timestamp, source, data_type, intent, extracted_data, conversation_id, sender, topic)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (entry_id, timestamp, source, data_type, intent, str(extracted_data), conversation_id, sender, topic))
        self.conn.commit()
        return {
            "id": entry_id,
            "timestamp": timestamp,
            "source": source,
            "data_type": data_type,
            "intent": intent,
            "extracted_data": extracted_data,
            "conversation_id": conversation_id,
            "sender": sender,
            "topic": topic,
        }
