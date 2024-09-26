def check_for_crisis(text):
    crisis_keywords = ["suicide", "self-harm", "end my life"]
    for keyword in crisis_keywords:
        if keyword in text.lower():
            return True
    return False
