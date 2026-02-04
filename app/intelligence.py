import re

KEYWORDS = ["urgent", "verify", "blocked", "suspend"]

def extract_intelligence(text, store):
    upi = re.findall(r"[a-zA-Z0-9.\-_]+@[a-zA-Z]+", text)
    phone = re.findall(r"\+91\d{10}", text)
    links = re.findall(r"https?://\S+", text)

    for k in KEYWORDS:
        if k in text.lower():
            store["suspiciousKeywords"].append(k)

    store["upiIds"].extend(upi)
    store["phoneNumbers"].extend(phone)
    store["phishingLinks"].extend(links)
