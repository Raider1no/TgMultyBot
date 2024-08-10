import requests
import json

class SessionInvalidException(Exception):
  pass

class SwarmAPI:
  client = requests.Session()
  client.headers.update({"user-agent": "MySwarmClient/1.0"})
  session = ""
  address = "http://127.0.0.1:7801"

  def get_session(self):
    response = self.client.post(f"{self.address}/API/GetNewSession", json={})
    self.session = response.json()["session_id"]

  def run_with_session(self, func):
    if not self.session:
      self.get_session()
    try:
      return func()
    except SessionInvalidException:
      self.get_session()
      return func()

  def generate_an_image(self, prompt):
    return self.run_with_session(lambda: self._generate_image(prompt))

  def _generate_image(self, prompt):
    data = {
      "images": 1,
      "session_id": self.session,
      "donotsave": False,
      "prompt": prompt,
      "negativeprompt": "(deformed, distorted, disfigured:1.3), poorly drawn, bad anatomy, wrong anatomy,missing background, extra limb, missing limb, floating limbs, (mutated hands and fingers:1.4), disconnected limbs, mutation, mutated, ugly, disgusting, blurry, amputation, poorly drawn feet, poorly drawn face, out of frame, extra limbs, disfigured, deformed, body out of frame, bad anatomy, watermark, signature, cut off, low contrast, underexposed, overexposed, bad art, beginner, amateur, distorted face.",
      "model": "jaga",
      "width": 1024,
      "height": 1024,
      "cfgscale": 4.5,
      "steps": 28,
      "sampler": "dpmpp_2m",
      "scheduler": "sgm_uniform",
      "seed": -1
    }
    response = self.client.post(f"{self.address}/API/GenerateText2Image", json=data)
    if "error_id" in response.json():
      raise SessionInvalidException()
    return response.json()["images"][0]


# SwarmAPI().generate_an_image("redhead girl, standing on the beach, realism, 8k")