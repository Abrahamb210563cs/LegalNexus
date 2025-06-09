# backend/train_llama.py

from transformers import LlamaTokenizer, LlamaForCausalLM, Trainer, TrainingArguments, DataCollatorForLanguageModeling
from datasets import load_dataset
import torch
import os

# Load tokenizer and model (7B version; change as needed)
model_name = "meta-llama/Llama-2-7b-hf"  # Must have access rights (accept Meta license!)
tokenizer = LlamaTokenizer.from_pretrained(model_name)
model = LlamaForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16, device_map="auto")

# Load your dataset
dataset = load_dataset("json", data_files={"train": "./data/sample_train.jsonl"}, split="train")

# Tokenize the dataset
def tokenize_fn(example):
    return tokenizer(example["text"], truncation=True, padding="max_length", max_length=512)

tokenized_dataset = dataset.map(tokenize_fn, batched=True)

# Training args
training_args = TrainingArguments(
    output_dir="./results",
    per_device_train_batch_size=1,
    gradient_accumulation_steps=4,
    num_train_epochs=2,
    logging_steps=10,
    save_steps=100,
    save_total_limit=2,
    fp16=True,  # Full 16-bit
    evaluation_strategy="no",
    report_to="none"
)

# Data collator
data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

# Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset,
    tokenizer=tokenizer,
    data_collator=data_collator
)

# Start training
trainer.train()
