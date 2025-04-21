from fastapi import FastAPI, Request
import logging
from slowapi.middleware import SlowAPIMiddleware

from .utils import generate_response
from .rate_limiting import limiter
from .logging import configure_logging, LogLevels
from fastapi.middleware.cors import CORSMiddleware


from pydantic import BaseModel

class PromptRequest(BaseModel):
    prompt: str


configure_logging(LogLevels.info)

app = FastAPI()

#Middlewares
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.state.limiter = limiter 
app.add_middleware(SlowAPIMiddleware)

@limiter.limit("10/minute")
@app.post('/generate')
async def generate(request: PromptRequest):
    prompt = request.prompt
    """Generate a response to a given prompt using the GPT-4 model.

    Args:
        request (Request): The request that triggered this endpoint.
        prompt (str): The prompt to generate a response for.

    Returns:
        dict: A dictionary with a single key "CHAT GPT:" and the generated response as the value.
            If there was an error generating the response, it will return a dictionary with a single
            key "error" and the error message as the value.

    Raises:
        HTTPException: If there was an error generating the response.
    """
    if prompt is None:
        logging.error("Prompt is None")
        return {"error": "Prompt is None"}

    logging.info("Prompt: " + str(prompt))
    response = generate_response(prompt)

    if not response:
        logging.error("Response is None")
        return {"error": "Response is None"}

    return {"CHAT GPT:": response}
