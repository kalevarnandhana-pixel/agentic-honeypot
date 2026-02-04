def agent_reply(history):
    last = history[-1]["text"].lower()

    if "blocked" in last:
        return "I’m really scared 😟 Why will my account be blocked?"
    if "upi" in last:
        return "I don’t understand this properly. Why do you need my UPI ID?"
    if "otp" in last:
        return "I haven’t received any OTP yet. Should I wait?"

    return "Can you please explain what I need to do?"
