import os
import httpx

pipe_path = os.getenv("AUDIO_PIPE", "/tmp/audio.pipe")
openai_api_key = os.getenv("OPENAI_API_KEY", "")

def send_to_openai(audio_data):
    print("[DEBUG] Audio data captured (not sent to OpenAI in this mock).")

print("🚀 Bridge started, waiting for audio...")

with open(pipe_path, "rb") as pipe:
    while True:
        data = pipe.read(1024)
        if data:
            send_to_openai(data)
