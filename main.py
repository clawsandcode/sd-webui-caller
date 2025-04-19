import requests, base64
import json
import random
from enum import Enum

from display import display_image

class Sampler(Enum):
    DPM_SDE = "DPM++ 2M SDE"
    DPM_KARRAS = "DPM++ 2M Karras"
    EULER_A = "Euler a"

loras = []
random_seed = random.randint(1, 10000000)

#Set prompts
negative_prompt_quality = "low quality"
negative_prompt_extra = "text, monochrome"
negative_prompt_variable = "sparks"

prompt_person = ""
prompt_pose=""
prompt_scene="A bright moon in the night sky"
prompt_quality="high quality, detailed"

#Set loras in .safetensors format and their strength
loras.append(("lora_1", 1))
loras.append(("lora_2", 0.7))
loras.append(("lora_3", 0.5))

#Set parameters
seed = random_seed
sampler = Sampler.DPM_SDE
cfg_scale = 5
steps = 20
width = 800
height = 1000
clip_skip = 1

sampler = sampler.value

text_loras = []
for lora in loras:
    text_loras.append(f"<{lora[0]}:{lora[1]}>")
prompt_loras = ','.join(text_loras)

negative_prompt = ','.join([negative_prompt_quality, negative_prompt_extra, negative_prompt_variable])
prompt = ','.join([prompt_person,prompt_pose,prompt_scene,prompt_loras, prompt_quality])

payload = {
    "prompt": prompt,
    "negative_prompt":negative_prompt,
    "sampler_name":sampler,
    "steps": steps,
    "cfg_scale": cfg_scale,
    "clip_skip": clip_skip,
    "seed":seed,
    "width":width,
    "height": height
}

#Send request to WebUI's txt2img endpoint
response = requests.post("http://127.0.0.1:7860/sdapi/v1/txt2img", json=payload)
print(f"Status code: {response.status_code}")
if response.ok:
    response_json = response.json()

    #Save JSON
    with open(f"json/response_data_{seed}.json", "w") as json_file:
        json.dump(response_json, json_file, indent=4)

    #Save image
    image_data = response_json["images"][0]
    image_path = f"output/output_{seed}.png"
    with open(image_path, "wb") as f:
        f.write(base64.b64decode(image_data))

    #Display image in image viewer
    display_image(image_path)
    print(f"Generated image seed: {seed}")