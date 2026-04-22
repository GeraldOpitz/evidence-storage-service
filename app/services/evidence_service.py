import uuid


class EvidenceService:

    def __init__(self):
        self.db = {}

    def save(self, payload: dict) -> str:
        evidence_id = str(uuid.uuid4())
        self.db[evidence_id] = payload
        return evidence_id

    def get(self, evidence_id: str) -> dict:
        if evidence_id not in self.db:
            raise ValueError("Evidence not found")

        return self.db[evidence_id]
