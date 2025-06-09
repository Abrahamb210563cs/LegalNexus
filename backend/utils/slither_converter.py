from datasets import load_dataset
import json
import os

def convert_slither_to_jsonl(split="small-multilabel", out_path="sample_contracts.jsonl"):
    print(f"🔍 Downloading and processing '{split}' split...")
    dataset = load_dataset("mwritescode/slither-audited-smart-contracts", split=split)

    os.makedirs("data/smart_contracts", exist_ok=True)
    output_file = f"data/smart_contracts/{out_path}"

    with open(output_file, "w", encoding="utf-8") as f:
        for row in dataset:
            prompt = {
                "instruction": "audit",
                "input": row["source_code"],
                "output": ", ".join(row["slither"]) if row["slither"] else "No vulnerabilities detected."
            }
            f.write(json.dumps(prompt) + "\n")

    print(f"✅ Done. Output saved to: {output_file}")

if __name__ == "__main__":
    convert_slither_to_jsonl()
