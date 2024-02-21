from modal import Image, Stub, web_endpoint
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import Optional
import random

class Audio(BaseModel):
    auth_token: Optional[str] = ""
    text: str

def random_id(n: int) -> str:
    """Generates a random ID of length n."""
    return "".join(random.choice("ZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba0123456789") for _ in range(n))

tts_image = (
    Image.debian_slim(python_version="3.10.8") 
    .pip_install(["edge-tts"])
)

with tts_image.imports():
    import edge_tts

stub = Stub("edge-tts")

@stub.function(image=tts_image)
@web_endpoint(method="POST")
async def create_audio(item: Audio):
    file_name = f"{random_id}.mp3"
    output_file = f"/tmp/{file_name}"

    communicate = edge_tts.Communicate(item.text, "en-AU-WilliamNeural")

    with open(output_file, "wb") as file:
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                file.write(chunk["data"])

    return FileResponse(path=output_file, media_type='audio/mpeg', filename=file_name)