import transformers
from datasets import load_dataset
from transformers import LlamaTokenizer, LlamaForCausalLM
from peft import LoraConfig, get_peft_model
from transformers import Trainer, TrainingArguments

def main():
    # Load tokenizer and base LLaMA model
    model_name = "decapoda-research/llama-7b-hf"  # Replace with your base model path if local
    tokenizer = LlamaTokenizer.from_pretrained(model_name)
    model = LlamaForCausalLM.from_pretrained(
        model_name,
        load_in_4bit=False,
        load_in_8bit=False,
        torch_dtype="float16",
        device_map="auto"
    )

    # PEFT (QLoRA) config - 16-bit precision
    peft_config = LoraConfig(
        r=16,
        lora_alpha=32,
        target_modules=["q_proj", "v_proj"],
        lora_dropout=0.05,
        bias="none",
        task_type="CAUSAL_LM"
    )

    model = get_peft_model(model, peft_config)
    model.print_trainable_parameters()

    # Load your dataset (make sure it's in instruction tuning JSONL format)
    dataset = load_dataset("json", data_files={"train": "data/smart_contracts/final_training.jsonl"}, split="train")

    # Tokenize the dataset
    def preprocess(examples):
        input_texts = [
            f"### Instruction:\n{ex['instruction']}\n### Input:\n{ex['input']}\n### Output:\n{ex['output']}"
            for ex in examples
        ]
        model_inputs = tokenizer(input_texts, truncation=True, max_length=512, padding="max_length")
        labels = model_inputs.input_ids.copy()
        model_inputs["labels"] = labels
        return model_inputs

    tokenized_dataset = dataset.map(preprocess, batched=True)

    # Training args
    training_args = TrainingArguments(
        output_dir="./llama_qlora_16bit",
        per_device_train_batch_size=4,
        gradient_accumulation_steps=4,
        num_train_epochs=3,
        learning_rate=2e-4,
        logging_steps=10,
        save_steps=100,
        evaluation_strategy="no",
        save_total_limit=2,
        fp16=True,
        optim="adamw_torch",
        report_to="none"
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset
    )

    trainer.train()

if __name__ == "__main__":
    main()
