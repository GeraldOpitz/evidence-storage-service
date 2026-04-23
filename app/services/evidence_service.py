import json
from app.clients.azure_blob_client import AzureBlobClient


class EvidenceService:

    def __init__(self):
        self.storage = AzureBlobClient()

    def save(self, payload: dict) -> str:
        return self.storage.save(json.dumps(payload))

    def get(self, evidence_id: str) -> dict:
        data = self.storage.get(evidence_id)
        return json.loads(data)
    
    def list_ids(self) -> list[dict]:
        return [{"id": evidence_id} for evidence_id in self.storage.list_ids()]
