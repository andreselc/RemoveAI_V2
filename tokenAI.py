from getpass import getpass
import os
import replicate
from dotenv import load_dotenv

load_dotenv()
REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")

input = {
  "video": open("./thatsMyOpinion.mp4", "rb")
}

output = replicate.run(
  "nateraw/video-background-remover:ac5c138171b04413a69222c304f67c135e259d46089fc70ef12da685b3c604aa",
  input=input
)
print(output)