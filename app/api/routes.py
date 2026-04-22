from fastapi import APIRouter

router = APIRouter(
    prefix="/api/evidence",
    tags=["evidence"]
)


@router.post("")
def create_evidence():
    return {"message": "not implemented yet"}


@router.get("/{evidence_id}")
def get_evidence(evidence_id: str):
    return {
        "message": "not implemented yet",
        "id": evidence_id
    }
