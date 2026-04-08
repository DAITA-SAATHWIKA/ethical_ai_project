from fastapi import FastAPI

app = FastAPI()

@app.post("/reset")
def reset():
    return {"status": "reset"}

@app.post("/step")
def step(input_text: str):

    text = input_text.lower()

    # Simple rule-based logic (SAFE)
    if "5" in text and "1" in text:
        decision = "minimize total casualties by saving more lives"
        ethical = 0.9
    elif "risk" in text:
        decision = "choose option with lower overall risk"
        ethical = 0.8
    elif "pedestrian" in text:
        decision = "prioritize minimizing harm to pedestrians"
        ethical = 0.85
    else:
        decision = "act to minimize harm"
        ethical = 0.75

    risk = min(len(text) / 100, 1.0)
    justification = 0.8

    return {
        "decision": decision,
        "scores": {
            "ethical": ethical,
            "risk": risk,
            "justification": justification
        }
    }

@app.get("/state")
def state():
    return {"status": "running"}