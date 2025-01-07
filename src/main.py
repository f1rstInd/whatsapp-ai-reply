from fastapi import FastAPI
from src.config.settings import Settings
from src.whatsapp.client import WhatsAppClient
from src.ai.model import AIModel

app = FastAPI()
settings = Settings()
whatsapp_client = WhatsAppClient()
ai_model = AIModel()

@app.post("/webhook")
async def webhook_handler(request: dict):
    """Handle incoming WhatsApp messages"""
    message = request.get("message")
    if message:
        # Process message and generate AI response
        response = ai_model.generate_response(message)
        await whatsapp_client.send_message(response)
    return {"status": "success"}
