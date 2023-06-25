from fastapi import APIRouter, Depends, HTTPException, status



router = APIRouter()


@router.get("/healthz", status_code=status.HTTP_200_OK)
async def health_check():
    return '{"status": "healthy"}'



