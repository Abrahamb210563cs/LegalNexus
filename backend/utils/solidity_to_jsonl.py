import os
import json

def scan_solidity_files(source_folder, output_file):
    with open(output_file, "w", encoding="utf-8") as out:
        for file in os.listdir(source_folder):
            if file.endswith(".sol"):
                path = os.path.join(source_folder, file)
                with open(path, "r", encoding="utf-8") as f:
                    code = f.read()
                    item = {
                        "instruction": "audit",
                        "input": code,
                        "output": "Add your manually written risk report here or use Slither output."
                    }
                    out.write(json.dumps(item) + "\n")

if __name__ == "__main__":
    os.makedirs("../../data/smart_contracts/raw", exist_ok=True)
    scan_solidity_files("../../data/smart_contracts/raw", "../../data/smart_contracts/manual_contracts.jsonl")
