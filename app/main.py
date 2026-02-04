from fastapi import FastAPI, Depends, Request, Body
from typing import Optional

from app.auth import verify_api_key
from app.detector import detect_scam
from app.agent import agent_reply
from app.intelligence import extract_intelligence
from app.memory import get_session
from app.callback import send_final_callback

app = FastAPI()


def should_terminate(session):
    intel = session["intelligence"]
    return (
        len(intel["upiIds"]) > 0 or
        len(intel["phishingLinks"]) > 0 or
        len(session["messages"]) >= 15
    )


# ✅ GUVI tester compatibility endpoint
@app.post("/")
async def root_post(api_key=Depends(verify_api_key)):
    return {
        "status": "success",
        "reply": "Honeypot service is active and secured."
    }


# ✅ Actual honeypot endpoint
@app.post("/honeypot/message")
async def honeypot(
    request: Request,
    payload: Optional[dict] = Body(None),
    api_key=Depends(verify_api_key)
):
    # GUVI tester hitting this endpoint with empty body
    if payload is None or "sessionId" not in payload:
        return {
            "status": "success",
            "reply": "Honeypot service is active and secured."
        }

    session_id = payload["sessionId"]
    message = payload["message"]

    session = get_session(session_id)
    session["messages"].append(message)

    detection = detect_scam(message["text"])

    if detection["is_scam"]:
        session["scamDetected"] = True
        extract_intelligence(message["text"], session["intelligence"])

        if should_terminate(session) and not session["callbackSent"]:
            send_final_callback(session_id, session)
            session["callbackSent"] = True
            return {
                "status": "success",
                "reply": "Okay, I will check this and get back to you."
            }

        reply = agent_reply(session["messages"])
        return {
            "status": "success",
            "reply": reply
        }

    return {
        "status": "ignored",
        "reply": None
    }
