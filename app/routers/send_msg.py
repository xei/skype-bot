import os

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field
from clients import skype



class RequestPayload(BaseModel):
    msg: str

router = APIRouter()


@router.post("/send-msg/{contact_or_chat}/{recipient}")
async def send_msg(contact_or_chat: str, recipient: str, payload: RequestPayload):
    """
    This is the main route in order tol send a message to a recipient.
    """
    if contact_or_chat == 'contact':
        chat = skype.get_skype_client().contacts[recipient].chat
    elif contact_or_chat == 'chat':
        chat = skype.get_skype_client().chats.chat(recipient)
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Just contact or chat!",
        )

    try:
        chat.sendMsg(payload.msg)
        return "SENT"
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )
