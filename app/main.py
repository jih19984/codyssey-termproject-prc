from fastapi import FastAPI

app = FastAPI(title="AI Chatbot")

@app.get("/health")
def health():
  return {"status": "ok"}

