sessions = {}

def get_session(session_id):
    if session_id not in sessions:
        sessions[session_id] = {
            "messages": [],
            "intelligence": {
                "bankAccounts": [],
                "upiIds": [],
                "phishingLinks": [],
                "phoneNumbers": [],
                "suspiciousKeywords": []
            },
            "scamDetected": False,
            "callbackSent": False
        }
    return sessions[session_id]
