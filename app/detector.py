SCAM_KEYWORDS = [
    "urgent", "verify", "blocked", "suspend",
    "upi", "bank", "otp", "kyc", "account"
]

def detect_scam(text: str):
    text = text.lower()
    matches = [k for k in SCAM_KEYWORDS if k in text]

    return {
        "is_scam": len(matches) >= 2,
        "confidence": min(len(matches) / 5, 1.0),
        "matched": matches
    }
