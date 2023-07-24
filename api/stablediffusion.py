import os
import replicate

class StableDiffusion:
    def __init__(self):
        self.prompt = "a vision of paradise. unreal engine"
    
    def get_url(self):
        model = replicate.models.get("stability-ai/stable-diffusion")
        version = model.versions.get("db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf")

        # https://replicate.com/stability-ai/stable-diffusion/versions/db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf#input
        inputs = {
            # Input prompt
            'prompt': self.prompt,

            # pixel dimensions of output image
            'image_dimensions': "768x768",

            # Specify things to not see in the output
            # 'negative_prompt': ...,

            # Number of images to output.
            # Range: 1 to 4
            'num_outputs': 1,

            # Number of denoising steps
            # Range: 1 to 500
            'num_inference_steps': 50,

            # Scale for classifier-free guidance
            # Range: 1 to 20
            'guidance_scale': 7.5,

            # Choose a scheduler.
            'scheduler': "DPMSolverMultistep",

            # Random seed. Leave blank to randomize the seed
            # 'seed': ...,
        }

        # https://replicate.com/stability-ai/stable-diffusion/versions/db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf#output-schema
        output = version.predict(**inputs)
        #print(output)

        output = str(output).replace("\'", "")
        output = str(output).replace("[", "")
        output = str(output).replace("]", "")
        
        return output

        #file_name = "output.png"

        #urllib.request.urlretrieve(output, file_name)
        
    def add_prompt(self, text):
        self.prompt = text    
