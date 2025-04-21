from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage, AssistantMessage
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv
import os
import logging

load_dotenv()

endpoint = "https://models.github.ai/inference"
model = "deepseek/DeepSeek-V3-0324"
token = os.getenv("GITHUB_API_KEY")

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

messages=[
    SystemMessage("You are a helpful assistant."),
]


def generate_response(prompt: str) -> str:
    """Generate a response to a given prompt using the GPT-4 model.

    Args:
        prompt (str): The prompt to generate a response for.

    Returns:
        str: The generated response.

    Raises:
        Exception: If there was an error generating the response. The error message is logged.
    """
    
    messages.append(
       UserMessage(str(prompt)),
    )
    try:
        response = client.complete(
            messages=messages,
            max_tokens=4096,
            model=model,
            temperature=0.8,
            top_p=0.1
        )
    except Exception as e:
        logging.error("Failed to generate response. With error: " + str(e))
        return None
    
    
    gpt_reply = response.choices[0].message.content
    logging.info("Response successfuly generated: " + str(gpt_reply))
    
    messages.append(
        AssistantMessage(gpt_reply),
    )
    return gpt_reply