from fastapi import APIRouter, HTTPException
from app.services.evidence_service import EvidenceService

router = APIRouter(
    prefix="/api/evidence",
    tags=["evidence"]
)

service = EvidenceService()


@router.post("")
def create_evidence(payload: dict):
    try:
        evidence_id = service.save(payload)
        return {"id": evidence_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{evidence_id}")
def get_evidence(evidence_id: str):
    try:
        data = service.get(evidence_id)
        return {"data": data}
    except ValueError:
        raise HTTPException(status_code=404, detail="Evidence not found")
