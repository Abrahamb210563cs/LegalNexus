import json
import os

def merge_jsonl_files(file_list, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as outfile:
        for path in file_list:
            if not os.path.isfile(path):
                print(f"⚠️ Skipping missing file: {path}")
                continue
            with open(path, "r", encoding="utf-8") as infile:
                for line in infile:
                    outfile.write(line)
    print(f"✅ Merged output saved to: {output_path}")

if __name__ == "__main__":
    file_list = [
        "data/smart_contracts/sample_contracts.jsonl",   # from slither_converter
        "data/smart_contracts/manual_contracts.jsonl"    # from solidity_to_jsonl
    ]
    merge_jsonl_files(file_list, "data/smart_contracts/final_training.jsonl")
