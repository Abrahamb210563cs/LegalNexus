# backend/inference_api.py

from fastapi import FastAPI, Request
from pydantic import BaseModel
from transformers import LlamaForCausalLM, LlamaTokenizer
import torch

app = FastAPI()

model_path = "./results"  # Path to your fine-tuned model

tokenizer = LlamaTokenizer.from_pretrained(model_path)
model = LlamaForCausalLM.from_pretrained(model_path, torch_dtype=torch.float16, device_map="auto")
model.eval()

class InputText(BaseModel):
    query: str

@app.post("/analyze/")
def analyze(input_data: InputText):
    prompt = f"Analyze this contract and summarize key points:\n\n{input_data.query}\n\nSummary:"
    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
    with torch.no_grad():
        outputs = model.generate(**inputs, max_new_tokens=300)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {"output": response.replace(prompt, "").strip()}
