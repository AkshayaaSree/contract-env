def grade(task, action_output):
    output = action_output.lower()
    score = 0.0

    if task["type"] == "clause_classification":
        if task["expected"]["label"] in output:
            score = 1.0

    elif task["type"] == "risk_detection":
        keywords = task["expected"]["risk_keywords"]
        matches = sum(1 for k in keywords if k in output)
        score = matches / len(keywords)

        if task["expected"]["severity"] in output:
            score += 0.2

    elif task["type"] == "contract_improvement":
        required = task["expected"]["must_include"]
        matches = sum(1 for k in required if k in output)
        score = matches / len(required)

        if "limit liability" in output or "cap liability" in output:
            score += 0.3

    return min(score, 1.0)