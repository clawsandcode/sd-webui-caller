Allows you to customize and send prompts to [AUTOMATIC1111's Stable Diffusion WebUI](https://github.com/AUTOMATIC1111/stable-diffusion-webui) via its REST API txt2img endpoint

Before launching the script make sure that webui.sh is running with the --api flag and the desired model is loaded.

Text prompts are split into multiple strings for easier customization. 

```
negative_prompt_quality = "low quality"
negative_prompt_extra = "text, monochrome"
negative_prompt_variable = "sparks"

prompt_person = ""
prompt_pose=""
prompt_scene="A bright moon in the night sky"
prompt_quality="high quality, detailed"
```

The parameters can be set directly through variables. The samplers are defined as enums. The output image is saved to the output directory and the response json is saved to the json directory.

This is just a concept, so not all parameters and samplers are present
