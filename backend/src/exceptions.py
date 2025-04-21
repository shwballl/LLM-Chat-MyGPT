from fastapi import HTTPException

class GPTError(HTTPException):
    """Base class for all GPT exceptions."""
    pass

class GPTResponseException(GPTError):
    def __init__(self):
        super().__init__(status_code=500, detail="Failed to generate response.")

class GPTPromptException(GPTError):
    def __init__(self):
        super().__init__(status_code=500, detail="Failed to generate prompt.")