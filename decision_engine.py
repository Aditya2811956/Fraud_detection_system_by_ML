def final_decision(rule_score, ml_prediction):

    final_risk = rule_score

    if ml_prediction == -1:
        final_risk += 30

    if final_risk > 70:
        status = "🚨 Fraud"
    elif final_risk > 40:
        status = "⚠️ Suspicious"
    else:
        status = "✅ Genuine"

    return status, final_risk