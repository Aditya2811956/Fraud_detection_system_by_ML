def rule_based_detection(speed, distance, user_weather, real_weather):
    risk = 0
    reasons = []

    # -------------------------------
    # Rule 1: No movement
    # -------------------------------
    if speed == 0:
        risk += 30
        reasons.append("No movement detected")

    # -------------------------------
    # Rule 2: Very low movement
    # -------------------------------
    if distance < 0.5:
        risk += 20
        reasons.append("Very low movement in last 10 minutes")

    # 🌧️ NEW RULE (MOST IMPORTANT)
    if user_weather != real_weather:
        risk += 40
        reasons.append("Weather mismatch detected")

    # -------------------------------
    # Rule 4: Suspicious pattern
    # -------------------------------
    if speed < 5 and distance < 0.2:
        risk += 20
        reasons.append("Suspicious behavior pattern detected")

    return risk, reasons