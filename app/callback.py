import requests

GUVI_URL = "https://hackathon.guvi.in/api/updateHoneyPotFinalResult"

def send_final_callback(session_id, session):
    payload = {
        "sessionId": session_id,
        "scamDetected": True,
        "totalMessagesExchanged": len(session["messages"]),
        "extractedIntelligence": session["intelligence"],
        "agentNotes": "Scammer used urgency, impersonation, and payment redirection tactics"
    }

    requests.post(GUVI_URL, json=payload, timeout=5)
