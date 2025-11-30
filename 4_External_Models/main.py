from google import genai
from google.genai import types
from PIL import Image

client = genai.Client()

prompt = (
    "Create a depth map of the image"
)

image = Image.open("image.png")

response = client.models.generate_content(
    model="gemini-3-pro-image-preview",
    contents=[prompt, image],
)

for part in response.parts:
    if part.text is not None:
        print(part.text)
    elif part.inline_data is not None:
        image = part.as_image()
        image.save("depthMap.png")