import os
import io
import warnings
from PIL import Image
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation

os.environ['STABILITY_HOST'] = 'grpc.stability.ai:443'
os.environ['STABILITY_KEY'] = 'sk-M7WEZAn38pQm0wB32MVoqiMI8L60tUSDMcmZsTxMB88yNP7A'

stability_api = client.StabilityInference(
    key=os.environ['STABILITY_KEY'], 
    engine="stable-diffusion-v1-5", 
)

User_input=input("Enter inspiration for Art: ")
answers = stability_api.generate(
    prompt=User_input,
)


for resp in answers:
    for artifact in resp.artifacts:
        if artifact.finish_reason == generation.FILTER:
            warnings.warn(
                "Your request activated the API's safety filters and could not be processed."
                "Please modify the prompt and try again.")
        if artifact.type == generation.ARTIFACT_IMAGE:
            img = Image.open(io.BytesIO(artifact.binary))
            img.save(str(User_input)+ ".png") 

        