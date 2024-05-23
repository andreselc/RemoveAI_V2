from getpass import getpass
import os
import replicate
from dotenv import load_dotenv
import requests

load_dotenv()
REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")

input = {
    "video": open("./thatsMyOpinion.mp4", "rb")
}

try:
    output_url = replicate.run(
        "nateraw/video-background-remover:ac5c138171b04413a69222c304f67c135e259d46089fc70ef12da685b3c604aa",
        input=input
    )
finally:
    input["video"].close()

def download_video(url, output_path):
    response = requests.get(url)
    response.raise_for_status()
    with open(output_path, 'wb') as f:
        f.write(response.content)

output_video_path = "./thatsMyOpinion2.mp4"
download_video(output_url, output_video_path)
print(f"Video descargado y guardado en {output_video_path}")