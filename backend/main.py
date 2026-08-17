from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from prompt_service import optimize_prompt

app = FastAPI(
    title="AI Prompt Optimizer",
    version="1.0"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request Model
class PromptRequest(BaseModel):
    prompt: str

# Home API
@app.get("/")
def home():
    return {
        "message": "Welcome to AI Prompt Optimizer API"
    }

# Prompt Optimizer API
@app.post("/generate-prompt")
def generate_prompt(data: PromptRequest):

    optimized = optimize_prompt(data.prompt)

    return {
        "original_prompt": data.prompt,
        "optimized_prompt": optimized
    }