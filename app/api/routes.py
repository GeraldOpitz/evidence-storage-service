from fastapi import APIRouter, HTTPException
from app.services.evidence_service import EvidenceService

router = APIRouter(
    prefix="/api/evidence",
    tags=["Evidence"]
)


def get_service() -> EvidenceService:
    return EvidenceService()


@router.get(
    "",
    summary="List evidence IDs",
    description="Returns the list of stored evidence identifiers."
)
def list_evidences():
    service = get_service()
    try:
        return {"items": service.list_ids()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post(
    "",
    summary="Create evidence",
    description="Stores a JSON payload as evidence and returns a generated evidence ID."
)
def create_evidence(payload: dict):
    service = get_service()
    try:
        evidence_id = service.save(payload)
        return {"id": evidence_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get(
    "/{evidence_id}",
    summary="Get evidence by ID",
    description="Retrieves a previously stored evidence payload using its ID."
)
def get_evidence(evidence_id: str):
    service = get_service()
    try:
        data = service.get(evidence_id)
        return {"data": data}
    except ValueError:
        raise HTTPException(status_code=404, detail="Evidence not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
