from fastapi import FastAPI, Request, Body

app = FastAPI()

@app.post("/reset")
async def reset(request: Request):
    try:
        await request.json()
    except:
        pass
    return {"status": "ok"}


@app.post("/step")
async def step(request: Request, data: dict = Body(default={})):
    try:
        body = await request.json()
    except:
        body = {}

    input_text = body.get("input_text") or data.get("input_text") or request.query_params.get("input_text", "")
    input_text = input_text.lower()

    if "5" in input_text and "1" in input_text:
        decision = "minimize total casualties"
        ethical = 0.9
    elif "risk" in input_text:
        decision = "choose lower risk option"
        ethical = 0.8
    else:
        decision = "minimize harm"
        ethical = 0.75

    risk = min(len(input_text) / 100, 1.0)
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
